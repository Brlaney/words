# utils.py
'''
    You can then ref these functions like:
        from scripts.utils import exit_program
        from scripts.utils import read_and_process_json
        from scripts.utils import get_audio_duration
    
    Functions in this file:
    
        *exit_program*: Ends the script gracefully.
        *read_and_process_json*: Reads a JSON file and returns the data as a list of objects.
        *get_audio_duration*: Returns the duration of the audio file in milliseconds.
        *create_markdown_links*: Generates markdown links for words and phrases based on provided data.
        *write_links_to_file*: Writes markdown links to a specified output file.
        *format_markdown*: Formats text by replacing placeholders with markdown formatting.
        *interpret_word_data_as_string*: Interprets structured word data and returns a raw markdown string.
        *save_audio_file*: Downloads and saves an audio file based on provided metadata.
        *categorize_audio_files*: Moves .wav files into appropriate directories and updates their paths in the JSON file.
'''
import sys
import json
import os 
import logging
import requests
from pydub import AudioSegment



# Configure logging
logging.basicConfig(filename='assets/reading_dict_jsons.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')



def exit_program():
    '''Ends the script gracefully.'''
    print('\nEnding script.. gracefully')
    sys.exit(0)



def read_and_process_json(file_path):
    '''Reads a JSON file and returns the data as a list of objects.'''
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f'f0 - File not found: {file_path}')
        return None



def get_audio_duration(file_path, file_name):
    '''
        Returns the duration of the audio file in milliseconds.
        
        :param file_path: Path to the audio file.
        :return: Duration of the audio in milliseconds.
    '''
    audio = AudioSegment.from_wav(file_path)
    duration_ms = len(audio)
    # logging.info(f'\nfile: {file_name}\nduration (ms): {duration_ms}')

    return duration_ms



def create_markdown_links(words_data):
    words_links = []
    phrases_links = []

    # Iterate through each word entry in the words data
    for word in words_data:
        if word.get("has_md", False):
            text = word.get("text", "")
            md_path = word.get("md_path", "")
            
            # Create the markdown link
            markdown_link = f'[{text}]({md_path})'
            
            # Append to words or phrases list based on md_path
            if 'md/words/' in md_path:
                words_links.append(markdown_link)
            elif 'md/phrases/' in md_path:
                phrases_links.append(markdown_link)

    # Sort the lists alphabetically
    words_links.sort()
    phrases_links.sort()

    return words_links, phrases_links



def write_links_to_file(words_links, phrases_links, output_file):
    # Format the output with sections and emojis
    output_content = "### Phrases 📃\n\n" + '\n'.join(f'- {link}' for link in phrases_links) + '\n\n---\n\n### Words 📃\n\n' + '\n'.join(f'- {link}' for link in words_links)
    
    with open(output_file, 'w', encoding='utf-8') as links_file:
        links_file.write(output_content)



def format_markdown(text):
    '''
        Replaces placeholders with markdown formatting and adds line returns.
        
        Args:
            text (str): The input text containing placeholders.
            
        Returns:
            str: The formatted text with markdown and line returns.
    '''
    # Replace the placeholders with appropriate markdown formatting
    formatted_text = text.replace('{bc}', '**:** ').replace('{it}', '*').replace('{/it}', '*').replace('{wi}', '`').replace('{/wi}', '`')

    # Add line returns after specific lines (e.g., after each key-value pair)
    # Here we split by line and rejoin with an extra newline after each line that ends with a colon
    lines = formatted_text.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Check if the line contains a key-value pair
        if line.endswith(':'):
            formatted_lines.append(line + '\n')  # Add a line return after the line
        else:
            formatted_lines.append(line)

    # Join the lines back together
    return '\n'.join(formatted_lines)



def interpret_word_data_as_string(text_data, data):
    '''
        Interpret word data and return a raw markdown string instead of writing to a file.
    
        Args:
            text_data (str): The word or phrase being processed.
            data (list): The structured data associated with the word or phrase.
    
        Returns:
            str: A raw markdown text string representation of the word or phrase.
    '''

    # Initialize the markdown content
    markdown_content = []

    # Generate markdown for structured data
    for entry in data:
        # Ensure that the entry is a dictionary
        if isinstance(entry, dict):
            word = entry.get('meta', {}).get('id', 'N/A')
            clean_word = format_markdown(word)
            markdown_content.append(f'# {clean_word}\n')

            part_of_speech = entry.get('fl', 'N/A')
            pronunciations = entry.get('hwi', {}).get('prs', [])
            pronunciation = pronunciations[0].get('mw', 'N/A') if pronunciations else 'N/A'
            audio_ref = pronunciations[0].get('sound', {}).get('audio', 'N/A') if pronunciations else 'N/A'

            clean_speech = format_markdown(part_of_speech)
            clean_pron = format_markdown(pronunciation)
            clean_ref = format_markdown(audio_ref)
            markdown_content.append(f'**Part of Speech:** {clean_speech}\n')
            markdown_content.append(f'**Pronunciation:** {clean_pron}\n')
            markdown_content.append(f'**Audio Reference:** {clean_ref}\n')

            # Process definitions
            if 'def' in entry:
                markdown_content.append('## Definitions:\n')
                for def_group in entry['def']:
                    for sense_group in def_group['sseq']:
                        for sense in sense_group:
                            if 'sense' in sense[0]:
                                definition_text = sense[1]['dt'][0][1] if 'dt' in sense[1] else 'N/A'
                                example_text = sense[1]['dt'][1][1][0]['t'] if len(sense[1].get('dt', [])) > 1 else None
                                
                                clean_definition = format_markdown(definition_text)
                                markdown_content.append(f'- {clean_definition}\n')
                                
                                if example_text:
                                    clean_example = format_markdown(example_text)
                                    markdown_content.append(f'  *Example:* {clean_example}\n')

            # Short definitions
            if 'shortdef' in entry:
                markdown_content.append('\n## Short Definitions:\n')
                for short_def in entry['shortdef']:
                    clean_shortdef = format_markdown(short_def)
                    markdown_content.append(f'- {clean_shortdef}\n')

            # Synonyms
            if 'syns' in entry:
                markdown_content.append('\n## Synonyms:\n')
                for synonym_group in entry['syns']:
                    for synonym in synonym_group.get('pt', []):
                        # Ensure synonym is a list and contains a dictionary
                        if isinstance(synonym, list) and len(synonym) > 0 and isinstance(synonym[0], dict):
                            if 'text' in synonym[0]:
                                clean_text = format_markdown(f"{synonym[0]['text']}")
                                markdown_content.append(f'- {clean_text}\n')


            # Related forms
            if 'uros' in entry:
                markdown_content.append('\n## Related Forms:\n')
                for form in entry['uros']:
                    related_word = form.get('ure', 'N/A')
                    related_pronunciation = form.get('prs', [{}])[0].get('mw', 'N/A')

                    clean_text = format_markdown(f'{related_word} ({related_pronunciation})')
                    markdown_content.append(f'- {clean_text}\n')
        else:
            logging.error(f'Unexpected entry format: {entry}')

    return ''.join(markdown_content)



'''
    This procedures takes in a single json object (would need to iterate over json file) and the output, save_directory.
'''
def save_audio_file(json_obj, save_dir):
    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Extract audio details from the JSON
    if json_obj['hwi']['prs']:  # Check if there are any pronunciation entries
        '''
            [language_code] - 2 letter ISO language code.
              en for all API references except the Spanish-English Dictionary.
              es for entries with a "lang": "es" metadata value in the Spanish-English Dictionary

            [country_code] - 2 letter ISO country code.
              us for all API references except the Spanish-English Dictionary.
              me for entries with a "lang": "es" metadata value in the Spanish-English Dictionary

            [format] - One of 3 audio formats supported for all audio values:
              mp3
              wav
              ogg

            [subdirectory] is determined as follows:
              if audio begins with "bix", the subdirectory should be "bix",
              if audio begins with "gg", the subdirectory should be "gg",
              if audio begins with a number or punctuation (eg, "_"), the subdirectory should be "number",
              otherwise, the subdirectory is equal to the first letter of audio.
        
            [base filename] - The name contained in audio.
        '''

        '''
            "prs" = pronunciation - the "prs" array may contain one or more pronunciation objects, each of which may contain the following members:
        
            "mw" : string	written pronunciation in Merriam-Webster format
            "l" : string	pronunciation label before pronunciation
            "l2" : string	pronunciation label after pronunciation
            "pun" : string	punctuation to separate pronunciation objects
            "sound" : object	audio playback information: the audio member contains the base filename for audio playback; the ref and stat members can be ignored.
            
        '''

        # Note: there COULD be multiple prs objects, see the [0] at eol
        pronounce_obj = json_obj.get('hwi', {}).get('prs', [{}])[0]

        if pronounce_obj is None:
            print('pronunciation obj is none')
            exit_program

        sound_obj = pronounce_obj.get('sound', {})

        if sound_obj is None:
            print('sound obj is none')
            exit_program

        audio_obj = sound_obj.get('audio')
        
        if audio_obj is None:
            print('audio obj is none')
            exit_program

        # Yay! Can continue ~
        meta_id_text = json_obj.get('meta', {}).get('id')
        
        
        if meta_id_text:
            print(f'success: {meta_id_text}')
            exit_program
        else:
            print(f'failed: {meta_id_text}')
            exit_program
        
                    
        language_code = 'en'  # Default to English
        country_code = 'us'   # Default to US
        output_format = 'wav' # Desired output format
        
        # Determine the base filename and subdirectory
        base_filename = audio_obj
        subdirectory = ''
        
        # Determine subdirectory based on audio filename
        if audio_obj.startswith('bix'):
            subdirectory = 'bix'
        elif audio_obj.startswith('gg'):
            subdirectory = 'gg'
        elif audio_obj[0].isdigit() or audio_obj[0] in ['_', '.', '-']:
            subdirectory = 'number'
        else:
            subdirectory = audio_obj[0].lower()  # Use the first letter of the audio filename
        
        base_endpoint = 'https://media.merriam-webster.com/audio/prons'
        
        # Construct the base URL
        full_url = f'{base_endpoint}/{language_code}/{country_code}/{output_format}/{subdirectory}/{base_filename}.{output_format}'
        
        # Define the local file path
        local_audio_path = os.path.join(save_dir, f'{base_filename}.{output_format}') 
            
        # Download the audio file
        try:
            response = requests.get(full_url)
            
            # Check for request errors
            response.raise_for_status()  
            
            with open(local_audio_path, 'wb') as audio_obj:
                audio_file.write(response.content)
            print(f'Audio file saved as: {local_audio_path}')
            
        except Exception as e:
            print(f'Error downloading audio file: {e}')
    else:
        logging.error(f"no info found for some json obj")
        print("No pronunciation entries found in the audio info.")



'''
    This function:
        - moves all .wav files in data/audio into their appropriate data/audio/words or ../phrases dir accordingly.
        - updates the words.json file with the new filepaths.
'''
def categorize_audio_files(source_dir, words_dir, phrases_dir, json_file_path):
    # Create destination directories if they don't exist
    os.makedirs(words_dir, exist_ok=True)
    os.makedirs(phrases_dir, exist_ok=True)

    # Load the words JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        words_data = json.load(json_file)

    # Iterate over each .wav file in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            # Determine if the filename is a word or phrase
            if '_' in filename or ' ' in filename:
                # Move to phrases directory
                destination_dir = phrases_dir
                audio_type = 'phrase'
            else:
                # Move to words directory
                destination_dir = words_dir
                audio_type = 'word'
            
            # Define the source and destination file paths
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

            # Move the file
            shutil.move(source_file, destination_file)
            print(f'Moving {filename} to {destination_dir}')

            # Update the audio path in the words data
            for entry in words_data:
                # Check if the audio path matches the old one
                if entry.get('audio_path') == os.path.join(source_dir, filename):
                    # Update to the new path
                    new_audio_path = os.path.join(destination_dir, filename)
                    entry['audio_path'] = new_audio_path
                    print(f'Updated audio path for {entry["text"]} to {new_audio_path}')

    # Save the updated words data back to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(words_data, json_file, indent=4)
        


def edit_audio(audio_path, text_value, duration=4, inc_vol=False):
    '''
        Function: edit_audio
        This function edits an audio file by setting its duration and optionally increasing its volume.
    
        Parameters:
        - audio_path (str): The path to the audio file to be edited.
        - text_value (str): The base name for the output file.
        - duration (int, optional): The duration (in seconds) to which the audio should be trimmed. Default is 4 seconds.
        - inc_vol (bool, optional): A flag to increase the volume of the audio. If True, the volume is doubled. Default is False.
    
        Returns:
        - output (str): The path of the output audio file.
    
        The function saves the edited audio file in the 'audio' directory with the provided text_value as the filename.
        If the 'inc_vol' parameter is set to True, the volume is increased by a factor of 2.
    '''
    audio_clip = AudioFileClip(audio_path).set_duration(duration)
    
    if inc_vol == True:
        output = audio_clip.volumex(2).write_audiofile(f'audio/{text_value}.wav')
    else:
        output = audio_clip.write_audiofile(f'audio/{text_value}.wav')
        
    return output



def get_audio_duration_new(file_path):
    '''
        Returns: 
            duration: the duration of the audio file in milliseconds.
            filename: the name of the audio file (if phrase, then camel case).
    
        :param file_path: Path to the audio file.
        :return: Duration of the audio in milliseconds.
    '''
    audio = AudioSegment.from_wav(file_path)
    duration_ms = len(audio)
    
    return duration_ms



def detect_json_structure(json_obj):
    '''
        This function checks the JSON structure and returns:
        - True - if the JSON is a list of strings.
        - False - if the JSON is structured as objects (list of dictionaries).
    '''
    if isinstance(json_obj, list) and json_obj:
        first_element = json_obj[0]
        
        if isinstance(first_element, str):
            return False
        
        elif isinstance(first_element, dict):
            return True

    return False



def is_phrase(text):
    ''' 
        Determines if a text is a phrase by checking for spaces. 
        TRUE = Phrase
        FALSE = Word
    '''
    return ' ' in text