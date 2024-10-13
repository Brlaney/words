import os
import io 
import sys 
import json 
import logging 
import numpy as np
from pydub import AudioSegment
from scripts.utils import exit_program
from scripts.utils import read_and_process_json

# Configure logging
logging.basicConfig(filename='assets/file_not_found.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

'''
'''
def detect_speech_end(file_path, 
                      silence_thresh=-50.0, 
                      chunk_size=10, 
                      silence_duration=500):
    
    logging.info('Starting speech detection.')
    
    # Load the audio file
    audio = AudioSegment.from_wav(file_path)
    logging.info(f'Loaded audio file: {file_path}')

    # Convert audio to numpy array (mono)
    samples = np.array(audio.get_array_of_samples())
    logging.info(f'Audio samples array shape: {samples.shape}')

    # Avoid divide by zero by adding a small epsilon value
    epsilon = 1e-10  # small value to prevent division by zero
    loudness = 20 * np.log10(np.abs(samples / (2.0**15)) + epsilon)
    logging.info(f'Calculated loudness array with {len(loudness)} elements.')

    # Detect sections of the file where the audio is above the threshold
    speech_chunks = []
    silent_chunks = 0
    logging.info(f'Starting speech detection with silence threshold: {silence_thresh}, chunk size: {chunk_size}, silence duration: {silence_duration}ms.')

    for i in range(0, len(loudness), chunk_size):
        chunk = loudness[i:i+chunk_size]
        avg_loudness = np.mean(chunk)
        logging.debug(f'Processing chunk {i // chunk_size}: average loudness = {avg_loudness}')
        
        if avg_loudness > silence_thresh:
            speech_chunks.append(i)
            silent_chunks = 0
            logging.debug(f'Speech detected at chunk {i // chunk_size}.')
        else:
            silent_chunks += 1
            logging.debug(f'Silent chunk detected. Silent chunk count: {silent_chunks}')

        # If we've had enough silence, break
        if silent_chunks * chunk_size >= silence_duration:
            logging.info(f'Silence detected for {silent_chunks * chunk_size}ms. Stopping detection.')
            break

    # Return the time (in ms) of the last 'speech' chunk
    end_of_speech = (speech_chunks[-1] * chunk_size) if speech_chunks else 0
    logging.info(f'End of speech detected at {end_of_speech}ms.')
    
    return end_of_speech

'''
    Returns the duration of the audio file in milliseconds.

    :param file_path: Path to the audio file.
    :return: Duration of the audio in milliseconds.
'''
def get_audio_duration(file_path, file_name):
    audio = AudioSegment.from_wav(file_path)
    duration_ms = len(audio)
    # logging.info(f'\nfile: {file_name}\nduration (ms): {duration_ms}')

    return duration_ms

'''
this procedure will iterate over the original words.json file and output the same data plus the audio files duration.
'''
def get_audio_duration_test(json_obj):
    data = []
    
    for item in json_obj:
        text = item['text']
        path = item['path']
        the_id = item['id']
        
        # Check if the path exists
        if os.path.exists(path):
            # Calculate duration if the file exists
            audio = AudioSegment.from_wav(path)
            duration_ms = len(audio)

            data.append({
                'id': the_id,
                'text': text,
                'duration': duration_ms,
                'path': path,
            })
        else:
            # Handle the case where the file doesn't exist
            logging.error(f'Failed to find the file using the given path.\nid={the_id} file={file_name}')
            
            data.append({
                'id': the_id,
                'text': text,
                'duration': 0,
                'path': path,
                'error': 'File does not exist' 
            })
            
    return data

'''
The script can be stopped by: 
KeyboardInterrupt exception. ie ctrl + c .
'''
json_obj = read_and_process_json('data/long-entries/before.json')

if json_obj:
    entries = []
    
    for item in json_obj:
        the_id = item['id']
        text = item['text']
        path = item['path']
        duration_before = item['duration']
        
        # Check if the path exists
        if os.path.exists(path):
            # Calculate duration if the file exists
            audio = AudioSegment.from_wav(path)
            duration_ms = len(audio)
            
            entries.append({
                'id': the_id,
                'text': text,
                'durationAfter': duration_ms,
                'durationBefore': duration_before,
                'path': path,
            })

    # print(f'final count: {count}')
    
    with open('after.json', 'w') as json_file:
        json.dump(entries, json_file, indent=4)
    
    # output_data = get_audio_duration_test(json_obj)
    # with open('test_output.json', 'w') as json_file:
    #     json.dump(output_data, json_file, indent=4)

# try:
        
    # while True:
            # for item in json_obj:
                # # Stop at index no. 2 to quickly test changes
                # if int(item['id']) == 3:
                #     exit_program()
                    
                # # speech_end_time = detect_speech_end(item['path'])
                # get_audio_duration(item['path'], item['text'])
        # else:
            # break

# except KeyboardInterrupt:
#     print('\nEnding script.. gracefully')
# finally:
#     print('Ending script.')
