import json

'''
textfile_to_json ~ procedure takes in two parameters: 
    input_file: a text file containing a list of words and filepaths to their associated audio file. A line could be a single word, or an entire phrase like "eye examination chart (audio\eye examination chart.wav)".
    output_file: the file path + name of the output json data.
'''
def textfile_to_json(input_file, output_file):
    data = []
    
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for idx, line in enumerate(lines):
        # Split the line into text and path parts
        text, path = line.strip().split(' (')
        path = path[:-1]  # Remove the closing parenthesis

        # Append the data in the required format
        data.append({
            "id": idx + 1,
            "text": text,
            "path": path
        })

    # Write the data to the output JSON file
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=2)

# Usage
input_file = 'words.txt'  # Replace with the path to your input file
output_file = 'words.json'  # Replace with your desired output file

# Call function w/ params
textfile_to_json(input_file, output_file)