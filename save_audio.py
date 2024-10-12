import os
import requests
from scripts.utils import read_and_process_json
from scripts.utils import save_audio_file

'''
    Refactor to:
        - Define the input directory (contains all json dict files) [now: data/dict/]
        - Iterate over each file in the dir
            - Iterate over each object within each individual file
            - Download, and save the audio file for each word/phrase (and all variants of it) with the unique name {data/audio/dict/unique_name.wav} 
'''

json_input = read_and_process_json('data/dict/mishap.json')

# Ensure json_input is a list and extract the first entry
if isinstance(json_input, list) and json_input:
    audio_data = json_input[0]  # Extract the first entry from the list
    
    save_audio_file(audio_data, 'data/audio/dictionary/')
else:
    print("Error: Invalid JSON structure or empty list.")
