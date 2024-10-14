'''
    This script: 
        - iterates over all audio and dict JSON files
        - determines if the file is a word or phrase
        - then moves to either the words or phrases directory accordingly
        - updates the filepath defined in words.json
'''
import os
import shutil
import json

def categorize_files(source_audio_dir, words_audio_dir, phrases_audio_dir, source_dict_dir, words_dict_dir, phrases_dict_dir, json_file_path):
    # Create destination directories if they don't exist
    os.makedirs(words_audio_dir, exist_ok=True)
    os.makedirs(phrases_audio_dir, exist_ok=True)
    os.makedirs(words_dict_dir, exist_ok=True)
    os.makedirs(phrases_dict_dir, exist_ok=True)

    # Load the words JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        words_data = json.load(json_file)

    # Helper function to categorize files based on their type (audio or JSON)
    def categorize_file(filename, source_dir, destination_dir, is_audio):
        # Define the source and destination file paths
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        # Move the file
        shutil.move(source_file, destination_file)
        print(f'Moving {filename} to {destination_dir}')

        if is_audio:
            # Update the audio path in the words data
            for entry in words_data:
                # Check if the audio path matches the old one
                if entry.get('audio_path') == source_file:
                    # Update to the new audio path
                    entry['audio_path'] = destination_file
                    print(f'Updated audio path for {entry["text"]} to {destination_file}')
        else:
            # Update the dict path in the words data
            for entry in words_data:
                # Check if the dict path matches the old one
                if entry.get('dict_path') == source_file:
                    # Update to the new dict path
                    entry['dict_path'] = destination_file
                    print(f'Updated dict path for {entry["text"]} to {destination_file}')

    # Iterate over each .wav file in the source audio directory
    for filename in os.listdir(source_audio_dir):
        if filename.endswith('.wav'):
            # Determine if the filename is a word or phrase
            if '_' in filename or ' ' in filename:
                # Move to phrases directory
                destination_dir = phrases_audio_dir
            else:
                # Move to words directory
                destination_dir = words_audio_dir
            
            # Categorize the audio file
            categorize_file(filename, source_audio_dir, destination_dir, is_audio=True)

    # Iterate over each JSON file in the source dict directory
    for filename in os.listdir(source_dict_dir):
        if filename.endswith('.json'):
            # Determine if the filename is a word or phrase
            if '_' in filename or ' ' in filename:
                # Move to phrases directory
                destination_dir = phrases_dict_dir
            else:
                # Move to words directory
                destination_dir = words_dict_dir
            
            # Categorize the JSON file
            categorize_file(filename, source_dict_dir, destination_dir, is_audio=False)

    # Save the updated words data back to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(words_data, json_file, indent=4)

# Define directories and JSON file paths
source_audio_dir = 'data/audio'
words_audio_dir = 'data/audio/words'
phrases_audio_dir = 'data/audio/phrases'
source_dict_dir = 'data/dict'
words_dict_dir = 'data/dict/words'
phrases_dict_dir = 'data/dict/phrases'
json_file_path = 'data/words.json'  # Path to your words.json file

# Call the function to categorize audio files and update the JSON file
categorize_files(source_audio_dir, words_audio_dir, phrases_audio_dir, source_dict_dir, words_dict_dir, phrases_dict_dir, json_file_path)

print('Audio and JSON files have been categorized and words.json has been updated.')
