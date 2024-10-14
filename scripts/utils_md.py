'''
'''
import sys
import json
import os 
import logging
import requests
from pydub import AudioSegment

# Configure logging
logging.basicConfig(filename='assets/utils_md.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_dir(filename, 
            type,
            for_my_audio=False, 
            for_json_dict=False, 
            for_audio_dict=False):

    if for_my_audio:
        return f'data/audio/{type}s/'
    if for_json_dict:
        return f'data/dict/json/{type}s/'
    if for_audio_dict:
        return f'data/dict/audio/{type}s/'
