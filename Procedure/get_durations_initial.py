import os
import json
from scripts.utils import get_audio_duration_new
from scripts.utils import is_phrase

def assemble_initial_json():
    clean_entries = []
    dirty_entries = []
    
    # Iterate over new batch of audio files
    for filename in os.listdir('new-audios/'):
        
        # Verify it's an audio file
        if filename.endswith('.wav'):
            
            # Strip file extension to get word or phrase
            word_or_phrase = filename.replace('.wav', '')
            this_duration = get_audio_duration_new(f'new-audios/{filename}')
            is_a_phrase = is_phrase(word_or_phrase)
            
            # Determine if it's a word or a phrase
            if is_a_phrase:
                the_type = 'phrase'
            else:
                the_type = 'word'
            
            entry = {
                'text': word_or_phrase,
                'duration': this_duration,
                'type': the_type,
                'filename': filename
            }
            
            # Separate into clean or dirty entries based on duration
            if this_duration > 4000:
                dirty_entries.append(entry)
            else:
                clean_entries.append(entry)
    
    # Compile the final output structure
    output = {
        'clean_entries': len(clean_entries),
        'dirty_entries': len(dirty_entries),
        'clean': clean_entries,
        'dirty': dirty_entries
    }
    
    return output


# Assemble the data and write it to a JSON file
output = assemble_initial_json()

with open('new-batch.json', 'w') as json_file:
    json.dump(output, json_file, indent=4)
