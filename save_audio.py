import os
import requests
from scripts.utils import read_and_process_json
from scripts.utils import save_audio_file
from scripts.utils import exit_program
from scripts.utils import detect_json_structure

'''
    Refactor to:
        - Define the input directory (contains all json dict files) [now: data/dict/]
        - Iterate over each file in the dir
            - Iterate over each object within each individual file
            - Download, and save the audio file for each word/phrase (and all variants of it) with the unique name {data/audio/dict/unique_name.wav} 
'''

'''
    We want to use the following json_input instead. 
    
    Goal is to iterate over each word or phrase 
    obj in json data and use the info in the data
    to create each needed filepath.

    {
        "id": 1,
        "text": "eye examination chart",
        "duration": 2601,
        "audio_file": "eye_examination_chart.wav",
        "dict_json": "eye_examination_chart.json",
        "mistake": true,
        "has_md": false,
        "md_path": "",
        "type": "phrase",
        "dict_audios": {
            "",
            ""
        }
    }
'''

words_json = read_and_process_json('data/words.json')

phrases_filepath = 'data/dict/json/phrases/'
words_filepath = 'data/dict/json/words/'

for obj in words_json:
    list_of_outputs = []
    
    if obj['id'] == 3:
        exit_program()
    
    txt = obj['text']
    json_dict = obj['dict_json']
    the_type = obj['type']
    mistake = obj['mistake']
    
    if mistake == False:
        print('not a mistake' + txt)
        
        if the_type == 'phrase':
            full_path = f'{phrases_filepath}{json_dict}'
            save_dir = 'data/dict/audio/phrases/'
        else:
            full_path = f'{words_filepath}{json_dict}'
            save_dir = 'data/dict/audio/words/'
        
        dict_json = read_and_process_json(full_path)
        
        for item in dict_json:
            print(item)
            
            audio_output = save_audio_file(
                json_obj=item, 
                save_dir=save_dir)
            
            list_of_outputs.append(audio_output)
    else:
        print('skip the mistake')