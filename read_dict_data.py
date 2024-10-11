import json, os, sys, logging

# Configure logging
logging.basicConfig(filename='assets/reading_dict_jsons.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

'''
Function to end the script gracefully
'''
def exit_program():
    print('\nEnding script.. gracefully')
    sys.exit(0)

''' 
Function to read and process a JSON file
'''
def read_and_process_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f'f0 - File not found: {file_path}')
        return None

'''
F**k this was a tough one
'''
def interpret_word_data(data, output_file):
    try:
        with open(output_file, 'a', encoding='utf-8') as f:  # 'a' to append to the file
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
                        
                        part_of_speech = entry.get('fl', 'N/A')
                        pronunciations = entry.get('hwi', {}).get('prs', [])
                        pronunciation = pronunciations[0].get('mw', 'N/A') if pronunciations else 'N/A'
                        audio_ref = pronunciations[0].get('sound', {}).get('audio', 'N/A') if pronunciations else 'N/A'

                        # Write the extracted information to the output file.
                        f.write(f'Word: {word}\n')
                        f.write(f'Part of Speech: {part_of_speech}\n')
                        f.write(f'Pronunciation: {pronunciation}\n')
                        f.write(f'Audio Reference: {audio_ref}\n')

                        # Check if definitions are present in the entry. 
                        if 'def' in entry:
                            f.write('\nDefinitions:\n')
                            for def_group in entry['def']:
                                for sense_group in def_group['sseq']:
                                    for sense in sense_group:
                                        if 'sense' in sense[0]:
                                            definition_text = sense[1]['dt'][0][1] if 'dt' in sense[1] else 'N/A'
                                            example_text = sense[1]['dt'][1][1][0]['t'] if len(sense[1].get('dt', [])) > 1 else None
                                            f.write(f'Definition: {definition_text}\n')
                                            if example_text:
                                                f.write(f'   Example: {example_text}\n')

                        # Check for short definitions under the 'shortdef' key.
                        if 'shortdef' in entry:
                            f.write('\nShort Definitions:\n')
                            for short_def in entry['shortdef']:
                                f.write(f'- {short_def}\n')

                        # Handle synonyms if present in the entry.
                        if 'syns' in entry:
                            f.write('\nSynonyms:\n')
                            for synonym_group in entry['syns']:
                                for synonym in synonym_group.get('pt', []):
                                    if 'text' in synonym[0]:
                                        f.write(synonym[0]['text'] + '\n')

                        # Check for related forms under 'uros'.
                        if 'uros' in entry:
                            f.write('\nRelated Forms:\n')
                            for form in entry['uros']:
                                related_word = form.get('ure', 'N/A')
                                related_pronunciation = form.get('prs', [{}])[0].get('mw', 'N/A')
                                f.write(f'{related_word} ({related_pronunciation})\n')
                    
                    else:
                        # Log the potential error or bug details to the log file
                        logging.error(f'l3 - last word: {last_word}')
                        logging.error(f'Unexpected entry format: {entry}\n')
                        logging.error(f'Data structure: {entry}')
                
                except Exception as e:
                    # Log the error details to the log file
                    logging.error(f'l2 - last word: {last_word}')
                    logging.error(f'Unexpected entry format: {entry}\n')
                    logging.error(f'exc: {e}')
                    
                f.write('\n' + '=' * 40 + '\n')            

    except Exception as e:
        # Log the error details to the log file
        logging.error(f'l1 - exc: {e}')
        logging.error(traceback.format_exc())  # Detailed stack trace

'''
Processes all of the json files then calls the interperate to text function
'''
def process_all_json_files_in_directory(directory, output_file):
    # Clear the file contents before writing new data
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n' + '=' * 40 + '\n')
    
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
                    interpret_word_data(json_data, output_file)
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
output_file = 'output.txt'
process_all_json_files_in_directory(json_directory, output_file)