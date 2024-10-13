# This file makes API calls to the Dictionary API
import requests 
import json 
import os
from dotenv import load_dotenv
from scripts.utils import exit_program, read_and_process_json

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

def output_resp_json(input_json_file, output_dir):
    json_obj = read_and_process_json(input_json_file)

    for item in json_obj:
        word_param = item['text']
        output = get_word_data(word_param=word_param)
        
        with open(f'{output_dir}{word_param}.json', 'w') as json_file:
            json.dump(output, json_file, indent=4)
            
'''
    Define the output_filepath parameter, then call the function to make the request and save the output
'''
# input_json = 'data/words.json'
# output_dir = 'data/dict/'
# output_resp_json(input_json, output_dir)

# Output for phrases
# data/dict/json/phrases/

# Output for words
# data/dict/json/words/

input_json = 'new-batch.json'
output_dir = 'data/dict/'
output_resp_json(input_json, output_dir)