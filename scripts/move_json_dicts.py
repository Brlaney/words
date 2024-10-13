import os
import json
import shutil
from scripts.utils import exit_program
from scripts.utils import read_and_process_json

def categorize_and_save_jsons(output_json_file):
    data = read_and_process_json(output_json_file)

    for item in data:
        text = item['text']
        filename = item['json_filename']
        the_type = item['type']
        
        current_path = f'data/dict/json/{filename}'
        
        if the_type == 'phrase':
            destination_path = 'data/dict/json/phrases/'
        else:
            destination_path = 'data/dict/json/words/'
        
        # Move the file
        shutil.move(current_path, destination_path)
        print(f'Moving {filename} to {destination_path}')

# Define input and output directories
json_data = 'new-output-batch.json'

# Run the categorization and saving process
categorize_and_save_jsons(json_data)
