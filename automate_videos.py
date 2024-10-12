# automate_videos.py
import json, io
from moviepy.editor import *
from scripts.utils import exit_program, read_and_process_json, get_audio_duration
import logging

# Configure logging
logging.basicConfig(filename='assets/automate_videos.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_video(audio_path, text_value, inc_vol):
    '''
    Takes in an audio file path and a text value.

    1. Loads the audio file using the filepath.
    2. Defines text to display.
    3. Creates a composite video clip setting the text to the center and a duration of 4 seconds long.
    4. Sets the loaded audio data to the composite video clip.
    5. And finally, writes an audio file using the text_value as the filename at 25 frames-per-second (fps).

    '''
    audio_clip = AudioFileClip(audio_path)

    txtClip = TextClip(text_value, 
                       color='white', 
                       font='Ariel', 
                       fontsize=88, 
                       bg_color='black')

    cvc = CompositeVideoClip([txtClip.set_pos('center')], 
        size=(1080, 720)).set_duration(3)

    if inc_vol == true:
        cvc.set_audio(audio_clip).volumex(2).write_videofile(f'videos/{text_value}.mp4', fps=25)
    else:
        cvc.set_audio(audio_clip).write_videofile(f'videos/{text_value}.mp4', fps=25)

def edit_audio(audio_path, text_value, duration=3):
    audio_clip = AudioFileClip(audio_path).set_duration(duration)
    audio_clip.volumex(2).write_audiofile(f'audio/{text_value}.wav')

# try:
#     json_obj = read_and_process_json('data/words.json')
# except:
#     print('womp')

'''
The script can be stopped by: 
KeyboardInterrupt exception. ie ctrl + c .
'''
try:
    while True:
        json_obj = read_and_process_json('data/words.json')
        json_new = read_and_process_json('data/long-entries/after.json')
        
        if json_obj and json_new:
            for item in json_obj:
                
                create_video(item['path'], item['text'])                
                # # Stop at index no. 2 to quickly test changes
                # if int(item['id']) == 1:
                #     exit_program()
        else:
            break

except KeyboardInterrupt:
    print('\nEnding script.. gracefully')
finally:
    print('Ending script.')
