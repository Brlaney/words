# utils.py
'''
You can then ref these functions like:
from scripts.utils import exit_program
from scripts.utils import read_and_process_json
from scripts.utils import get_audio_duration
'''
import sys
import json
import os 
import logging

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