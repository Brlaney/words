import json
import os
import logging
from scripts.utils import exit_program
from scripts.utils import read_and_process_json
from scripts.utils import detect_json_structure

# Configure logging
logging.basicConfig(filename='assets/logs/validate_paths.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')



def process_all_json_files_in_directory(directory, output_file):
    output_data = []
    
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f'Processing file: {filename}')
            
            # Load and interpret JSON data
            try:
                json_data = read_and_process_json(file_path)
                correct_structure = detect_json_structure(json_data)
                
                # If the structure is not correct (i.e., a list of strings)
                if not correct_structure:
                    all_entries = json_data if isinstance(json_data, list) else []
                    word_or_phrase = filename.replace('.json', '')
                    
                    output_data.append({
                        "word_or_phrase": word_or_phrase,
                        "filename": filename,
                        "correct_structure": correct_structure,
                        "suggestions": all_entries
                    })
                
            except json.JSONDecodeError as e:
                logging.error(f'JSON Decode Error in {filename}: {e}')
            except Exception as e:
                logging.error(f'Error processing {filename}: {e}')
    
    # Write the result to an output JSON file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(output_data, out_file, indent=4)

'''
    Define your directory containing the dictionary word .json files.
    Define the output filename.
    Call the function **process_all_json_files_in_directory**.
'''
json_directory = 'data/dict/'  # The directory with the JSON files
output_file = 'output.json'    # Output file to store results

process_all_json_files_in_directory(json_directory, output_file)
