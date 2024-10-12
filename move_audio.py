import os
import shutil
import json

def categorize_audio_files(source_dir, words_dir, phrases_dir, json_file_path):
    # Create destination directories if they don't exist
    os.makedirs(words_dir, exist_ok=True)
    os.makedirs(phrases_dir, exist_ok=True)

    # Load the words JSON file
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        words_data = json.load(json_file)

    # Iterate over each .wav file in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.wav'):
            # Determine if the filename is a word or phrase
            if '_' in filename or ' ' in filename:
                # Move to phrases directory
                destination_dir = phrases_dir
                audio_type = 'phrase'
            else:
                # Move to words directory
                destination_dir = words_dir
                audio_type = 'word'
            
            # Define the source and destination file paths
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

            # Move the file
            shutil.move(source_file, destination_file)
            print(f'Moving {filename} to {destination_dir}')

            # Update the audio path in the words data
            for entry in words_data:
                # Check if the audio path matches the old one
                if entry.get('audio_path') == os.path.join(source_dir, filename):
                    # Update to the new path
                    new_audio_path = os.path.join(destination_dir, filename)
                    entry['audio_path'] = new_audio_path
                    print(f'Updated audio path for {entry["text"]} to {new_audio_path}')

    # Save the updated words data back to the JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(words_data, json_file, indent=4)

# Define directories and JSON file path
source_audio_dir = 'data/audio'
words_audio_dir = 'data/audio/words'
phrases_audio_dir = 'data/audio/phrases'
json_file_path = 'data/words.json'  # Path to your words.json file

# Call the function to categorize audio files and update the JSON file
categorize_audio_files(source_audio_dir, words_audio_dir, phrases_audio_dir, json_file_path)

print('Audio files have been categorized and words.json has been updated.')
