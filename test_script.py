import os
import json

def categorize_and_save_jsons(input_dir, words_dir, phrases_dir):
    # Create output directories if they don't exist
    os.makedirs(words_dir, exist_ok=True)
    os.makedirs(phrases_dir, exist_ok=True)

    # Iterate over all JSON files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            
            try:
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)

                    # Check if the data has a 'type' key and determine the output directory
                    if isinstance(data, list) and len(data) > 0 and 'type' in data[0]:
                        entry_type = data[0]['type']  # Check the type from the first entry
                        
                        if entry_type == 'word':
                            output_path = os.path.join(words_dir, filename)
                        elif entry_type == 'phrase':
                            output_path = os.path.join(phrases_dir, filename)
                        else:
                            print(f"Unknown type in {filename}: {entry_type}. Skipping.")
                            continue

                        # Save the JSON file to the corresponding directory
                        with open(output_path, 'w') as output_file:
                            json.dump(data, output_file, indent=4)
                            print(f"Saved '{filename}' to '{output_path}'")

            except Exception as e:
                print(f"Error processing '{filename}': {e}")

# Define input and output directories
input_dir = 'data/dict/json/'
words_dir = 'data/dict/json/words/'
phrases_dir = 'data/dict/json/phrases/'

# Run the categorization and saving process
categorize_and_save_jsons(input_dir, words_dir, phrases_dir)
