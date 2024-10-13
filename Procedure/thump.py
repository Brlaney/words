import json
import os

def determine_type(text):
    # A simple heuristic to determine if the text is a word or a phrase
    # Adjust this logic based on your criteria for phrases vs. words
    return "phrase" if " " in text else "word"

def transform_words_json(words_json_path):
    # Load the existing words.json file
    with open(words_json_path, 'r') as words_file:
        words_data = json.load(words_file)

    # Transform the data by adding the type field
    for entry in words_data:
        entry['type'] = determine_type(entry['text'])

    # Write the updated data back to words.json
    with open(words_json_path, 'w') as words_file:
        json.dump(words_data, words_file, indent=4)

# Define the path to the words.json file
words_json_path = 'data/words.json'

# Run the function to transform the words.json
transform_words_json(words_json_path)

print("words.json has been transformed successfully.")
