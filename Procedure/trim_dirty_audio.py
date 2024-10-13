import os
import json
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def load_dirty_entries(json_file):
    """
    Load the dirty entries from the given JSON file.
    
    :param json_file: Path to the JSON file containing the data.
    :return: List of dirty entries.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data.get('dirty', [])

"""
    Detect where the audio should be trimmed by removing trailing silence.
    
    :param file_path: Path to the audio file to be trimmed.
    :param output_path: Path to save the trimmed audio. If None, overwrites original file.
    :param silence_thresh: Silence threshold in dBFS (decibels relative to full scale).
    :param min_silence_len: Minimum length of silence in milliseconds.
    :return: Trimmed audio segment.
"""
def trim_audio(file_path, 
               output_path=None, 
               silence_thresh=-50, 
               min_silence_len=500, 
               duration=5000):

    audio = AudioSegment.from_wav(file_path)
    
    # Detect the non-silent chunks in the audio (start and end times in milliseconds)
    nonsilent_ranges = detect_nonsilent(
        audio_segment=audio, 
        min_silence_len=min_silence_len, 
        silence_thresh=silence_thresh)
    
    if nonsilent_ranges:
        # Get the start and end times of the actual audio content (non-silent portion)
        start_trim, end_trim = nonsilent_ranges[0][0], nonsilent_ranges[-1][1]
        print(f'Start, end trim before: {start_trim}, {end_trim}')
        
        if start_trim > 500:
            start_trim -= 500
        elif start_trim < 500:
            start_trim = 0
        
        if end_trim + 800 < duration:
            end_trim += 800
        
        print(f'Start, end trim after: {start_trim}, {end_trim}')
        trimmed_audio = audio[start_trim:end_trim]

        # Save the trimmed audio
        if output_path is None:
            output_path = file_path  # Overwrite the original file
        trimmed_audio.export(out_f=output_path, format="wav")
        
        print(f"Trimmed and saved: {output_path}")
        return trimmed_audio
    else:
        print(f"No non-silent part detected for {file_path}")
        return None

def process_dirty_entries(json_file):
    """
        Process the dirty entries by trimming unnecessary silence from their audio files.
        
        :param json_file: Path to the JSON file with dirty entries.
    """
    dirty_entries = load_dirty_entries(json_file)
    
    # For initial testing
    # output = trim_audio(
    #     file_path='toot/get_bogged_down.wav', 
    #     silence_thresh=-38, 
    #     min_silence_len=500)

    for entry in dirty_entries:
        filename = entry['filename']
        duration = entry['duration']
        file_path = os.path.join('new-audios', filename)
        
        if os.path.exists(file_path):
            print(f"Processing: {file_path}")
            
            # Call the trim_audio function to trim the silence
            trim_audio(file_path=file_path, 
                       silence_thresh=-38, 
                       min_silence_len=500, 
                       duration=duration)
        else:
            print(f"File not found: {file_path}")

# Example usage
process_dirty_entries('new-batch.json')
print('finished')