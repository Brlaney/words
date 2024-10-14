'''
'''
import sys
import json
import os 
import logging
import requests
from pydub import AudioSegment

# Configure logging
logging.basicConfig(filename='assets/utils-files.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

