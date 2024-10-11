# This file makes API calls to the Dictionary API
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

DICT_API_KEY = os.getenv('DICT_API_KEY')

'''
exit_program(): is just used to end the script `gracefully`
'''
def exit_program():
    print('\nEnding script.. gracefully')
    sys.exit(0)

'''
Takes in a file path and outputs an entire json array of objects
'''
def read_and_process_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

def get_word_data(word_param):
    base_url = 'https://www.dictionaryapi.com'
    endpoint = '/api/v3/references/collegiate/json/'
    
    try:
        # Make the API request
        response = requests.get(f'{base_url}{endpoint}{word_param}?key={DICT_API_KEY}')
        
        # Raise exception for HTTP errors
        response.raise_for_status()  
        data = response.json() # Parse the JSON data
        
        return data
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# word_param = 'voluminous'
json_obj = read_and_process_json('data/words.json')

for item in json_obj:
    word_param = item['text']
    output = get_word_data(word_param=word_param)
    
    with open(f'data/dict/{word_param}.json', 'w') as json_file:
        json.dump(output, json_file, indent=4)