'''
  Goal:
    To output the perfect markdown using one json file
'''
import os
import json
from scripts.utils import read_and_process_json
from scripts.utils import interpret_word_data_as_string

the_word = 'mishap'
json_data = read_and_process_json(f'data/dict/{the_word}.json')

markdown_string = interpret_word_data_as_string(
  the_word,   # the word
  json_data)  # the data

print(markdown_string)
