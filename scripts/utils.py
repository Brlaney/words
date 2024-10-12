# utils.py
'''
You can then ref these functions like:
from scripts.utils import exit_program
from scripts.utils import read_and_process_json
from scripts.utils import get_audio_duration
'''

import sys
import json
import os 
import logging

# Configure logging
logging.basicConfig(filename='assets/reading_dict_jsons.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def exit_program():
    '''Ends the script gracefully.'''
    print('\nEnding script.. gracefully')
    sys.exit(0)

def read_and_process_json(file_path):
    '''Reads a JSON file and returns the data as a list of objects.'''
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        logging.error(f'f0 - File not found: {file_path}')
        return None

def get_audio_duration(file_path, file_name):
    '''
        Returns the duration of the audio file in milliseconds.
        
        :param file_path: Path to the audio file.
        :return: Duration of the audio in milliseconds.
    '''
    audio = AudioSegment.from_wav(file_path)
    duration_ms = len(audio)
    # logging.info(f'\nfile: {file_name}\nduration (ms): {duration_ms}')

    return duration_ms

def format_markdown(text):
    '''
        Replaces placeholders with markdown formatting and adds line returns.
        
        Args:
            text (str): The input text containing placeholders.
            
        Returns:
            str: The formatted text with markdown and line returns.
    '''
    # Replace the placeholders with appropriate markdown formatting
    formatted_text = text.replace('{bc}', '**:** ').replace('{it}', '*').replace('{/it}', '*').replace('{wi}', '`').replace('{/wi}', '`')

    # Add line returns after specific lines (e.g., after each key-value pair)
    # Here we split by line and rejoin with an extra newline after each line that ends with a colon
    lines = formatted_text.split('\n')
    formatted_lines = []
    
    for line in lines:
        # Check if the line contains a key-value pair
        if line.endswith(':'):
            formatted_lines.append(line + '\n')  # Add a line return after the line
        else:
            formatted_lines.append(line)

    # Join the lines back together
    return '\n'.join(formatted_lines)