import json
import os
import sys
import logging
from scripts.utils import exit_program, read_and_process_json

# Configure logging
logging.basicConfig(filename='assets/logs/reading_dict_jsons.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

'''
    F**k this was a tough one
'''
def interpret_word_data(text_data, data, output_dir):
    try:
        file_name_output = f'data/md/{text_data}.md'
        
        with open(file_name_output, 'w', encoding='utf-8') as f:
            
            # Check if the data is a list of strings
            if isinstance(data, list) and all(isinstance(item, str) for item in data):
                f.write('List of words:\n')
                for word in data:
                    f.write(f'- {word}\n')
                f.write('\n' + '=' * 40 + '\n')
                return
            
            # Otherwise, process as if it's a list of dictionary entries
            for entry in data:
                last_word = ''  # Initialize last_word as an empty string
                
                try:
                    # Ensure that the entry is a dictionary
                    if isinstance(entry, dict):
                        ''' Extract word information '''
                        word = entry.get('meta', {}).get('id', 'N/A')
                        last_word = word
                            
                        # Create a Markdown file for the word
                        f.write(f"# {word}\n\n")
                        
                        # Extracting word information
                        part_of_speech = entry.get('fl', 'N/A')
                        pronunciations = entry.get('hwi', {}).get('prs', [])
                        pronunciation = pronunciations[0].get('mw', 'N/A') if pronunciations else 'N/A'
                        audio_ref = pronunciations[0].get('sound', {}).get('audio', 'N/A') if pronunciations else 'N/A'

                        # Write the extracted information to the Markdown file
                        f.write(f"**Part of Speech:** {part_of_speech}\n")
                        f.write(f"**Pronunciation:** {pronunciation}\n")
                        f.write(f"**Audio Reference:** {audio_ref}\n\n")

                        # Check for definitions
                        if 'def' in entry:
                            f.write("## Definitions:\n")
                            for def_group in entry['def']:
                                for sense_group in def_group['sseq']:
                                    for sense in sense_group:
                                        if 'sense' in sense[0]:
                                            definition_text = sense[1]['dt'][0][1] if 'dt' in sense[1] else 'N/A'
                                            example_text = sense[1]['dt'][1][1][0]['t'] if len(sense[1].get('dt', [])) > 1 else None
                                            f.write(f"- {definition_text}\n")
                                            if example_text:
                                                f.write(f"  *Example:* {example_text}\n")

                        # Short definitions
                        if 'shortdef' in entry:
                            f.write("\n## Short Definitions:\n")
                            for short_def in entry['shortdef']:
                                f.write(f"- {short_def}\n")

                        # Synonyms
                        if 'syns' in entry:
                            f.write("\n## Synonyms:\n")
                            for synonym_group in entry['syns']:
                                for synonym in synonym_group.get('pt', []):
                                    if 'text' in synonym[0]:
                                        f.write(f"- {synonym[0]['text']}\n")

                        # Related forms
                        if 'uros' in entry:
                            f.write("\n## Related Forms:\n")
                            for form in entry['uros']:
                                related_word = form.get('ure', 'N/A')
                                related_pronunciation = form.get('prs', [{}])[0].get('mw', 'N/A')
                                f.write(f"- {related_word} ({related_pronunciation})\n")
                    else:
                        logging.error(f'l3 - last word: {last_word}')
                        logging.error(f'Unexpected entry format: {entry}\n')
                        logging.error(f'Data structure: {entry}')
                                                
                except Exception as e:
                    logging.error(f'l2 - last word: {last_word}')
                    logging.error(f'Unexpected entry format: {entry}\n')
                    logging.error(f'exc: {e}')
    except Exception as e:
        logging.error(f'l1 - exc: {e}')
        logging.error(traceback.format_exc())  # Detailed stack trace

'''
    Processes all of the json files then calls the interperate to text function
'''
def process_all_json_files_in_directory(directory, output_file):
    '''
        Clear the file contents before writing new data.
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n' + '=' * 40 + '\n')
    '''
    j = 1
    
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        logging.info(f'index: {j}, file: {filename}')
        
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f'Processing index: {j}, file: {filename}')
            
            # Load and interpret JSON data
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    json_data = json.load(file)
                    interpret_word_data(filename.replace('.json', ''), json_data, output_file)
                except json.JSONDecodeError as e:
                    logging.error(f'l0 - JSON Decode Error in {filename}: {e}')
                except Exception as e:
                    logging.error(f'l0 - Error processing {filename}: {e}')
        j += 1

'''
    Define your dir containing the dictionary word .json files.
    Define the output filename.
    Call the function **process_all_json_files_in_directory**
'''
json_directory = 'data/dict/'
output_dir = 'md/'  # output_file = 'output.txt'
process_all_json_files_in_directory(json_directory, output_dir)
