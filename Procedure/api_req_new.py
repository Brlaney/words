import requests
import json
import os
from dotenv import load_dotenv
from scripts.utils import exit_program
from scripts.utils import read_and_process_json

load_dotenv()
DICT_API_KEY = os.getenv('DICT_API_KEY')

def get_word_data(word_param):
    base_url = 'https://www.dictionaryapi.com'
    endpoint = '/api/v3/references/collegiate/json/'

    try:
        response = requests.get(f'{base_url}{endpoint}{word_param}?key={DICT_API_KEY}')
        response.raise_for_status()  
        data = response.json()
        
        return data
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def process_json_and_get_word_data(input_json_file, 
                                   output_json_file, 
                                   output_dir):
  
    json_obj = read_and_process_json(input_json_file)
    output_data = []

    for item in json_obj:
        word_param = item['text']
        output = get_word_data(word_param=word_param)

        # Create the new entry for the output JSON
        new_entry = {
            'text': item['text'],
            'duration': item['duration'],
            'type': item['type'],
            'audio_filename': item['filename'],
            'json_filename': f"{item['filename'].replace('.wav', '')}.json"  # Create JSON filename from audio filename
        }
        
        output_data.append(new_entry)
        
        # Save the individual word data response to a JSON file
        with open(f'{output_dir}{new_entry["json_filename"]}', 'w') as json_file:
            json.dump(output, json_file, indent=4)
    
    # Save the transformed output data to new-output-batch.json
    with open(output_json_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"Successfully created {output_json_file} with {len(output_data)} entries.")


# Define input and output paths
input_json = 'new-batch.json'
output_json_file = 'new-output-batch.json'
output_dir = 'data/dict/json/'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process the input JSON and get word data
process_json_and_get_word_data(input_json, output_json_file, output_dir)
