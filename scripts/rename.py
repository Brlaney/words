'''
    This script will read words.json and rename all audio filepaths and actual audio filenames in data/audio to be camel case.
'''
import os
import json
import logging
from scripts.utils import exit_program, read_and_process_json

# Configure logging
logging.basicConfig(filename='assets/logs/rename_audio_files.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def rename_audio_files_and_update_json(audio_dir, json_file):
    # Load the JSON data
    words_data = read_and_process_json(json_file)

    if not words_data:
        logging.error(f"Error: Could not read JSON file: {json_file}")
        exit_program()
    
    for word_entry in words_data:
        # Get current audio path
        current_audio_path = word_entry['audio_path']
        original_audio_filename = os.path.basename(current_audio_path)
        
        # Construct the new filename by replacing spaces with underscores
        new_audio_filename = original_audio_filename.replace(' ', '_')
        new_audio_path = os.path.join(audio_dir, new_audio_filename)
        
        # Get the full path of the current and new audio file
        original_full_path = os.path.join(audio_dir, original_audio_filename)
        new_full_path = os.path.join(audio_dir, new_audio_filename)
        
        # Check if the original file exists
        if os.path.exists(original_full_path):
            # Rename the audio file
            os.rename(original_full_path, new_full_path)
            print(f"Renamed: {original_audio_filename} -> {new_audio_filename}")
            logging.info(f"Renamed: {original_audio_filename} -> {new_audio_filename}")
        else:
            logging.warning(f"File not found: {original_full_path}")
            continue
        
        # Update the audio_path field in the JSON object
        word_entry['audio_path'] = new_audio_path
    
    # Save the updated JSON data back to the file
    with open(json_file, 'w', encoding='utf-8') as json_outfile:
        json.dump(words_data, json_outfile, indent=4)

    print(f"All files processed and {json_file} updated successfully.")
    logging.info(f"All files processed and {json_file} updated successfully.")

# Define the directory containing the audio files
# Define the path to the JSON file
# Call the function to rename files and update JSON
audio_directory = 'data/audio/'  # Directory where the audio files are stored
json_file_path = 'data/words.json'  # Path to the words JSON file
rename_audio_files_and_update_json(audio_directory, json_file_path)
