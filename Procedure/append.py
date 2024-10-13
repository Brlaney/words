import json
import os
from scripts.utils import read_and_process_json
from scripts.utils import detect_json_structure

def append_to_words_json(words_json_path, output_batch_json_path):
    # Load the existing words.json file
    if os.path.exists(words_json_path):
        with open(words_json_path, 'r') as words_file:
            words_data = json.load(words_file)
    else:
        words_data = []

    # Load the new-output-batch.json file
    with open(output_batch_json_path, 'r') as output_batch_file:
        new_entries = json.load(output_batch_file)

    # Determine the next ID based on existing words data
    next_id = max(entry['id'] for entry in words_data) + 1 if words_data else 1

    # Transform and append the new entries
    for entry in new_entries:
        mistake = detect_json_structure(entry)
      
        # Transform to the target format
        transformed_entry = {
            "id": next_id,
            "text": entry["text"],
            "duration": entry["duration"],
            "audio_path": entry["audio_filename"],  # Changed field name to audio_path
            "dict_path": f"data/dict/{entry['json_filename']}",  # Adjust dict_path
            "mistake": mistake,
            "has_md": False,
            "md_path": ""
        }

        # Append the transformed entry to the words data
        words_data.append(transformed_entry)
        next_id += 1  # Increment the ID for the next entry

    # Write the updated words data back to words.json
    with open(words_json_path, 'w') as words_file:
        json.dump(words_data, words_file, indent=4)

# Define the paths to the JSON files
words_json_path = 'data/words.json'
output_batch_json_path = 'new-output-batch.json'

# Run the function to append to words.json
append_to_words_json(words_json_path, output_batch_json_path)

print("Entries appended to words.json successfully.")
