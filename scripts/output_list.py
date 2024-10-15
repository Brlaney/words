import json
import os
import logging
from scripts.utils import exit_program, read_and_process_json

# Read the JSON data from 'output.json'
data = read_and_process_json('output.json')
output = []

if data:
    for item in data:
        structure = item['correct_structure']
        filename = item['filename']
        
        # Add filenames where structure is False
        if not structure:
            output.append(filename)
    
    # Write the output list to 'output_2.json' with indentation
    with open('output_2.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4)
