'''
    Refactor to:
        - Define the input directory (contains all json dict files) [now: data/dict/]
        - Iterate over each file in the dir
            - Iterate over each object within each individual file
            - Download, and save the audio file for each word/phrase (and all variants of it) with the unique name {data/audio/dict/unique_name.wav} 
'''
import os
import requests
from scripts.utils import read_and_process_json
from scripts.utils import save_audio_file
from scripts.utils import exit_program

# Define the input directory (contains all json dict files)
phrases_filepath = 'data/dict/json/phrases/'
words_filepath = 'data/dict/json/words/'

# Read the existing words.json data
words_json = read_and_process_json('data/words.json')

# Iterate over each object in words.json
for obj in words_json:
    list_of_outputs = []
    
    # Check if the current object has an ID of 3 and exit if so
    if obj['id'] == 3:
        exit_program()
    
    txt = obj['text']
    json_dict = obj['dict_json']
    the_type = obj['type']
    mistake = obj['mistake']
    
    if not mistake:  # Only process if it's not marked as a mistake
        print(f'Processing: {txt}')
        
        # Determine the full path and saving directory based on type
        if the_type == 'phrase':
            full_path = f'{phrases_filepath}{json_dict}'
            save_dir = 'data/dict/audio/phrases/'
        else:  # it's a word
            full_path = f'{words_filepath}{json_dict}'
            save_dir = 'data/dict/audio/words/'
        
        # Read the corresponding dict JSON file
        dict_json = read_and_process_json(full_path)

        # Skip if dict_json is None
        if dict_json is None:
            print(f'Skipping {txt}: dict_json is None')
            continue

        # Iterate over each item in the dict JSON
        for item in dict_json:
            # print(item)
            
            # Attempt to save the audio file and capture the output
            audio_output = save_audio_file(json_obj=item, save_dir=save_dir)
            if audio_output:  # Check if the output is valid
                list_of_outputs.append(audio_output)
        
        # Update the current object with the new field containing list_of_outputs
        obj['dict_audios'] = list_of_outputs
    
    else:
        print(f'Skipping mistake: {txt}')

# Rewrite the updated words_json back to the words.json file
with open('data/words.json', 'w') as json_file:
    json.dump(words_json, json_file, indent=4)

print("Finished processing and updating words.json.")
