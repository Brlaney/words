import json, io
from moviepy.editor import *

'''
exit_program(): is just used to end the script `gracefully`
'''
def exit_program():
    print('\nEnding script.. gracefully')
    sys.exit(0)

'''
Takes in a file path and outputs an entire json array of objects
'''
def read_and_process_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data

'''
Takes in an audio file path and a text value.

1. Loads the audio file using the filepath.
2. Defines text to display.
3. Creates a composite video clip setting the text to the center and a duration of 4 seconds long.
4. Sets the loaded audio data to the composite video clip.
5. And finally, writes an audio file using the text_value as the filename at 25 frames-per-second (fps).

'''
def create_video(audio_path, text_value):
    audio_clip = AudioFileClip(audio_path)

    txtClip = TextClip(text_value, 
                       color='white', 
                       font='Ariel', 
                       fontsize=88, 
                       bg_color='black')

    cvc = CompositeVideoClip([txtClip.set_pos('center')], 
        size=(1080, 720)).set_duration(3)

    cvc.set_audio(audio_clip).volumex(2).write_videofile(f'videos/{text_value}.mp4', fps=25)


def edit_audio(audio_path, text_value, duration=3):
    audio_clip = AudioFileClip(audio_path).set_duration(duration)
    # edited_clip = CompositeAudioClip(audio_clip).set_duration(duration)
    audio_clip.volumex(2).write_audiofile(f'audio/{text_value}.wav')

data = {
    'id': 20,
    'text': 'soared',
    'duration': 13003,
    'path': 'audio/soared.wav'
}

edit_audio(data['path'], data['text'])

'''
The script can be stopped by: 
KeyboardInterrupt exception. ie ctrl + c .
'''
# try:
#     while True:
#         json_obj = read_and_process_json('data/words.json')
        
#         if json_obj:
#             for item in json_obj:
                
#                 # Stop at index no. 2 to quickly test changes
#                 if int(item['id']) == 1:
#                     exit_program()
                
#                 create_video(item['path'], item['text'])
#         else:
#             break

# except KeyboardInterrupt:
#     print('\nEnding script.. gracefully')
# finally:
#     print('Ending script.')
