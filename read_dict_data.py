import json
import os
import sys

# Function to end the script gracefully
def exit_program():
    print('\nEnding script.. gracefully')
    sys.exit(0)

# Function to read and process a JSON file
def read_and_process_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return None

# F**k this was a tough one
def interpret_word_data(data, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:  # 'a' to append to the file
        for entry in data:
            # Ensure that the entry is a dictionary
            if isinstance(entry, dict):
                # Extract word information
                word = entry.get('meta', {}).get('id', 'N/A')
                part_of_speech = entry.get('fl', 'N/A')
                pronunciations = entry.get('hwi', {}).get('prs', [])
                pronunciation = pronunciations[0].get('mw', 'N/A') if pronunciations else 'N/A'
                audio_ref = pronunciations[0].get('sound', {}).get('audio', 'N/A') if pronunciations else 'N/A'
                
                f.write(f'Word: {word}\n')
                f.write(f'Part of Speech: {part_of_speech}\n')
                f.write(f'Pronunciation: {pronunciation}\n')
                f.write(f'Audio Reference: {audio_ref}\n')
                
                # Extract definitions and examples
                if 'def' in entry:
                    f.write('\nDefinitions:\n')
                    for def_group in entry['def']:
                        for sense_group in def_group['sseq']:
                            for sense in sense_group:
                                if 'sense' in sense[0]:
                                    definition_text = sense[1]['dt'][0][1] if 'dt' in sense[1] else 'N/A'
                                    example_text = sense[1]['dt'][1][1][0]['t'] if len(sense[1].get('dt', [])) > 1 else None
                                    f.write(f'Definition: {definition_text}\n')
                                    if example_text:
                                        f.write(f'   Example: {example_text}\n')
                
                # Extract short definitions if available
                if 'shortdef' in entry:
                    f.write('\nShort Definitions:\n')
                    for short_def in entry['shortdef']:
                        f.write(f'- {short_def}\n')
                
                # Handle other sections like idioms or synonyms if present
                if 'syns' in entry:
                    f.write('\nSynonyms:\n')
                    for synonym_group in entry['syns']:
                        for synonym in synonym_group.get('pt', []):
                            if 'text' in synonym[0]:
                                f.write(synonym[0]['text'] + '\n')
                
                if 'uros' in entry:
                    f.write('\nRelated Forms:\n')
                    for form in entry['uros']:
                        related_word = form.get('ure', 'N/A')
                        related_pronunciation = form.get('prs', [{}])[0].get('mw', 'N/A')
                        f.write(f'{related_word} ({related_pronunciation})\n')
            
            else:
                f.write(f'Unexpected entry format: {entry}\n')
            
            f.write('\n' + '='*40 + '\n')

def process_all_json_files_in_directory(directory, output_file):
    # Clear the file contents before writing new data
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('')

    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f'Processing file: {file_path}')
            
            # Load and interpret JSON data
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    json_data = json.load(file)
                    interpret_word_data(json_data, output_file)
                except json.JSONDecodeError as e:
                    print(f'Error decoding JSON in {filename}: {e}')
                except Exception as e:
                    print(f'Error processing {filename}: {e}')

# Example usage
json_directory = 'data/dict/'
output_file = 'output.txt'
process_all_json_files_in_directory(json_directory, output_file)