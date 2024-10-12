'''
    This script will read words.json and mistakes.json and renames all data/dict json files to be camel case.
'''
import os
import json
import logging
from scripts.utils import exit_program, read_and_process_json

# Configure logging
logging.basicConfig(filename='assets/logs/rename_dict_files.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_mistake_in_mistakes_json(mistakes_data, word_or_phrase):
    '''
    Checks if the given word or phrase exists in the mistakes.json file.
    Returns True if the word is found, False otherwise.
    '''
    for mistake_entry in mistakes_data:
        if mistake_entry['word_or_phrase'] == word_or_phrase:
            return True
    return False

def rename_dict_files_and_update_json(dict_dir, json_file, mistakes_file):
    # Load the JSON data from words.json
    words_data = read_and_process_json(json_file)
    
    # Load the mistakes.json file
    mistakes_data = read_and_process_json(mistakes_file)

    if not words_data:
        logging.error(f"Error: Could not read JSON file: {json_file}")
        exit_program()
    
    if not mistakes_data:
        logging.error(f"Error: Could not read mistakes.json file: {mistakes_file}")
        exit_program()

    for word_entry in words_data:
        # Get current text
        word_or_phrase = word_entry['text']
        
        # Create the new filename by replacing spaces with underscores
        new_dict_filename = word_or_phrase.replace(' ', '_') + '.json'
        new_dict_path = os.path.join(dict_dir, new_dict_filename)
        
        # Check if there's a corresponding .json file in data/dict/
        original_dict_filename = word_or_phrase + '.json'
        original_full_path = os.path.join(dict_dir, original_dict_filename)
        new_full_path = os.path.join(dict_dir, new_dict_filename)
        
        if os.path.exists(original_full_path):
            # Rename the dictionary file
            os.rename(original_full_path, new_full_path)
            print(f"Renamed: {original_dict_filename} -> {new_dict_filename}")
            logging.info(f"Renamed: {original_dict_filename} -> {new_dict_filename}")
        else:
            logging.warning(f"File not found: {original_full_path}")
        
        # Update dict_path field in the words_data
        word_entry['dict_path'] = new_dict_path
        
        # Check if the word or phrase exists in mistakes.json
        word_entry['mistake'] = check_mistake_in_mistakes_json(mistakes_data, word_or_phrase)
    
    # Write the updated words_data to the words.json file
    with open(json_file, 'w', encoding='utf-8') as json_outfile:
        json.dump(words_data, json_outfile, indent=4)

    # Update filenames in mistakes.json
    for mistake_entry in mistakes_data:
        original_mistake_filename = mistake_entry['word_or_phrase'] + '.json'
        new_mistake_filename = mistake_entry['word_or_phrase'].replace(' ', '_') + '.json'
        
        if os.path.exists(os.path.join(dict_dir, original_mistake_filename)):
            # Rename the mistake file
            os.rename(os.path.join(dict_dir, original_mistake_filename),
                      os.path.join(dict_dir, new_mistake_filename))
            mistake_entry['dict_path'] = os.path.join(dict_dir, new_mistake_filename)
    
    # Write the updated mistakes_data back to the mistakes.json file
    with open(mistakes_file, 'w', encoding='utf-8') as mistakes_outfile:
        json.dump(mistakes_data, mistakes_outfile, indent=4)

    print(f"All files processed and {json_file} & {mistakes_file} updated successfully.")
    logging.info(f"All files processed and {json_file} & {mistakes_file} updated successfully.")

# Define the directory containing the dictionary files
dict_directory = 'data/dict/'  # Directory where the dictionary .json files are stored

# Define the path to the words.json file
json_file_path = 'data/words.json'  # Path to the words JSON file

# Define the path to the mistakes.json file
mistakes_file_path = 'data/mistakes.json'  # Path to the mistakes JSON file

# Call the function to rename files and update JSON
rename_dict_files_and_update_json(dict_directory, json_file_path, mistakes_file_path)
