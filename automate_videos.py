# automate_videos.py
import io
import json 
import logging
from moviepy.editor import *
from scripts.utils import exit_program
from scripts.utils import read_and_process_json
from scripts.utils import get_audio_duration_2
from scripts.utils_md import get_dir

# Configure logging
logging.basicConfig(filename='assets/automate_videos.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_video(words_json, inc_vol=True):
    '''
        Takes in an audio file path and a text value.

        1. Loads the audio file using the filepath.
        2. Defines text to display.
        3. Creates a composite video clip setting the text to the center and a duration of 4 seconds long.
        4. Sets the loaded audio data to the composite video clip.
        5. And finally, writes an audio file using the text_value as the filename at 25 frames-per-second (fps).

    '''
    
    ''' Parse the words_json data '''
    the_id = words_json['id']
    text = words_json['text']
    the_type = words_json['type']
    audio_file = words_json['audio_file']
    
    audio_path = get_dir(filename=audio_file, 
                         type=the_type, 
                         for_my_audio=True)
    
    print(audio_path)
    print(audio_file)
    
    audio_fullpath = f'{audio_path}{audio_file}'
    print(audio_fullpath)
    
    audio_clip = AudioFileClip(audio_fullpath)
    audio_duration = int(audio_clip.duration + 3.75)

    txtClip = TextClip(text, 
                       color='white', 
                       font='Ariel', 
                       fontsize=88, 
                       bg_color='black')

    cvc = CompositeVideoClip(
        [txtClip.set_pos('center')], 
        size=(540, 360)).set_duration(audio_duration)

    output_path = f'data/videos/{the_type}s/{text}.mp4'

    if inc_vol == True:
        cvc.set_audio(audio_clip).volumex(2).write_videofile(output_path, fps=25)
        
    elif inc_vol == False:
        cvc.set_audio(audio_clip).write_videofile(output_path, fps=25)
    
    if the_id == 198:
        print('That was the last index, 190, wicked men.')
        exit_program()

'''
    The script can be stopped by: 
    KeyboardInterrupt exception. ie ctrl + c .
'''
try:
    while True:
        ''' The infamous words (or phrases) json '''
        json_obj = read_and_process_json('data/words.json')
        
        ''' filter the file by >= 106 - the crash point '''
        filtered_obj = [item for item in json_obj if item.get('id', 0) >= 126]
        
        ''' This batch, need to exclude these from AMPING the volumex(2).
            They've already had the same function ran on them. '''
        id_list = [110, 113]

        if filtered_obj:
            for item in filtered_obj:
                the_id = item['id']

                if the_id in id_list:
                    '''These were already increased w/ volumex(2)'''
                    inc_volume = False
                else:
                    '''These need to be increased w/ volumex(2)'''
                    inc_volume = True
                    
                if the_id >= 125:
                    '''These were recorded with ~max vol already'''
                    inc_volume = False
                
                print(f'Creating video for id: {the_id}')
                create_video(words_json=item, inc_vol=inc_volume)
                
except KeyboardInterrupt:
    exit_program()
    print('\nEnding script.. gracefully')
finally:
    print('Ending script.')