# This file makes API calls to the Dictionary API
import json, os

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


file_before = 'data/dict/barely.json'
file_after = 'data/long-entries/after.json'

before_data = read_and_process_json(file_before)
after_data = read_and_process_json(file_after)

