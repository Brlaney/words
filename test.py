import os
import json
from scripts.utils import read_and_process_json
from scripts.utils import interpret_word_data_as_string

json_data = read_and_process_json('mishap.json')

markdown_string = interpret_word_data_as_string('mishap', json_data)
print(markdown_string)
