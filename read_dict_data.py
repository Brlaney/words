import json
import os
import logging

from scripts.utils import exit_program 
from scripts.utils import read_and_process_json
from scripts.utils import format_markdown
from scripts.utils import is_phrase
from scripts.utils_md import get_dir

# Configure logging
logging.basicConfig(filename='assets/logs/reading_dict_jsons.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def interpret_word_data(text_data, data, the_type, snake_case):
    try:
        '''
            words_output_dir
            phrases_output_dir
        '''
        # Determine the directory for words or phrases
        output_dir = phrases_output_dir if is_phrase(text_data) else words_output_dir

        # Create the Markdown file name based on the word or phrase
        file_name_output = f'md/{the_type}s/{snake_case}.md'
        
        has_md = False
        md_path = ''  # Default empty path for markdown
        
        # Check if the data is a list of strings (no markdown generation)
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            has_md = False
            md_path = ''
        else:
            # Generate markdown for structured data
            with open(file_name_output, 'w', encoding='utf-8') as f:
                has_md = True
                md_path = file_name_output
                
                for entry in data:
                    # Ensure that the entry is a dictionary
                    if isinstance(entry, dict):
                        word = entry.get('meta', {}).get('id', 'N/A')

                        clean_word = format_markdown(word)
                        f.write(f'# {clean_word}\n\n')
                        
                        part_of_speech = entry.get('fl', 'N/A')
                        pronunciations = entry.get('hwi', {}).get('prs', [])
                        pronunciation = pronunciations[0].get('mw', 'N/A') if pronunciations else 'N/A'
                        audio_ref = pronunciations[0].get('sound', {}).get('audio', 'N/A') if pronunciations else 'N/A'

                        clean_speech = format_markdown(part_of_speech)
                        clean_pron = format_markdown(pronunciation)
                        clean_ref = format_markdown(audio_ref)
                        f.write(f'**Part of Speech:** {clean_speech}\n\n')
                        f.write(f'**Pronunciation:** {clean_pron}\n\n')
                        f.write(f'**Audio Reference:** {clean_ref}\n\n')

                        # Process definitions
                        if 'def' in entry:
                            f.write('## Definitions:\n')
                            for def_group in entry['def']:
                                for sense_group in def_group['sseq']:
                                    for sense in sense_group:
                                        if 'sense' in sense[0]:
                                            definition_text = sense[1]['dt'][0][1] if 'dt' in sense[1] else 'N/A'
                                            example_text = sense[1]['dt'][1][1][0]['t'] if len(sense[1].get('dt', [])) > 1 else None
                                            
                                            clean_definition = format_markdown(definition_text)
                                            f.write(f'- {clean_definition}\n')
                                            
                                            if example_text:
                                                clean_example = format_markdown(example_text)
                                                f.write(f'  *Example:* {clean_example}\n')

                        # Short definitions
                        if 'shortdef' in entry:
                            f.write('\n## Short Definitions:\n')
                            for short_def in entry['shortdef']:
                                clean_shortdef = format_markdown(short_def)
                                f.write(f'- {clean_shortdef}\n')

                        # Synonyms
                        if 'syns' in entry:
                            f.write('\n## Synonyms:\n')
                            for synonym_group in entry['syns']:
                                for synonym in synonym_group.get('pt', []):
                                    if 'text' in synonym[0]:
                                        clean_text = format_markdown(f'{synonym[0]['text']}')
                                        f.write(f'- {clean_text}\n')

                        # Related forms
                        if 'uros' in entry:
                            f.write('\n## Related Forms:\n')
                            for form in entry['uros']:
                                related_word = form.get('ure', 'N/A')
                                related_pronunciation = form.get('prs', [{}])[0].get('mw', 'N/A')

                                clean_text = format_markdown(f'{related_word} ({related_pronunciation})')
                                f.write(f'- {clean_text}\n')

                    else:
                        logging.error(f'Unexpected entry format: {entry}')

        return has_md, md_path  # Return markdown status and path
    
    except Exception as e:
        logging.error(f'Error generating markdown for {text_data}: {e}')
        return False, ''


def process_all_json_files_in_directory(words_file, mistakes_file):
    words_data = read_and_process_json(words_file)
    mistakes_data = read_and_process_json(mistakes_file)

    if not words_data:
        logging.error(f'Error: Could not read JSON file: {words_file}')
        exit_program()

    for item in words_data:
        word_or_phrase = item['text']
        dict_filename = item['dict_json']
        the_type = item['type']
        
        dict_file_path = get_dir(filename=dict_filename, 
                                 type=the_type, 
                                 for_json_dict=True)
        
        if os.path.exists(dict_file_path):
            try:
                with open(dict_file_path, 'r', encoding='utf-8') as file:
                    json_data = json.load(file)

                    # Interpret the word data and generate markdown if needed
                    has_md, md_path = interpret_word_data(
                        word_or_phrase, 
                        json_data,
                        the_type,
                        snake_case=dict_filename.replace('.json', '')
                    )

                    # Update the word entry with dict_path, mistake, has_md, and md_path
                    item['dict_path'] = dict_file_path
                    item['has_md'] = has_md
                    item['md_path'] = md_path if has_md else ''

                    # Check if the word or phrase exists in mistakes.json
                    item['dict_resp'] = not any(m['text'] == word_or_phrase for m in mistakes_data)

            except Exception as e:
                logging.error(f'Error processing {dict_filename}: {e}')
        else:
            logging.warning(f'File not found: {dict_file_path}')

    # Write the updated words_data back to the words.json file
    with open(words_file, 'w', encoding='utf-8') as json_outfile:
        json.dump(words_data, json_outfile, indent=4)

    print(f'All files processed and {words_file} updated successfully.')


'''
     words_md_dir = 'md/words/'      # Output directory for word markdown files
     phrases_md_dir = 'md/phrases/'  # Output directory for phrase markdown files
     json_directory = 'data/dict/'   # Directory containing dictionary .json files

     Ensure directories exist
     os.makedirs(words_md_dir, exist_ok=True)
     os.makedirs(phrases_md_dir, exist_ok=True)
'''
# Define directories and file paths
words_json_file = 'data/words.json'  # Path to words.json file
mistakes_json_file = 'data/mistakes.json'  # Path to mistakes.json file

# Process the dictionary files and update words.json
process_all_json_files_in_directory(words_json_file, mistakes_json_file)