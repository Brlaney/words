import os
import json
from scripts.utils import get_audio_duration_new
from scripts.utils import is_phrase

def snake_case(text):
    """Convert a phrase to snake_case format."""
    return text.lower().replace(' ', '_').replace('-', '_')

def assemble_final_json():
    entries = []
    
    # Iterate over new batch of audio files
    for filename in os.listdir('new-audios/'):
        
        # Verify it's an audio file
        if filename.endswith('.wav'):
            
            # Strip file extension to get word or phrase
            word_or_phrase = filename.replace('.wav', '')
            this_duration = get_audio_duration_new(f'new-audios/{filename}')
            is_a_phrase = is_phrase(word_or_phrase)
            
            # Determine if it's a word or a phrase
            the_type = 'phrase' if is_a_phrase else 'word'
            
            # If it's a phrase, rename the file to snake_case
            if the_type == 'phrase':
                new_filename = f"{snake_case(word_or_phrase)}.wav"
                
                # Rename the file in the file system
                os.rename(f'new-audios/{filename}', f'new-audios/{new_filename}')
                filename = new_filename  # Update the filename to the new one
            
            # Create an entry for each audio file
            entry = {
                'text': word_or_phrase,
                'duration': this_duration,
                'type': the_type,
                'filename': filename
            }
            
            entries.append(entry)
    
    return entries


# Assemble the data and write it to a JSON file
output = assemble_final_json()

with open('final-batch.json', 'w') as json_file:
    json.dump(output, json_file, indent=4)

print(f"Successfully created final-batch.json with {len(output)} entries.")
