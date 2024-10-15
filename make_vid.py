# automate_videos.py
import io
import json 
from moviepy.editor import *
from scripts.utils import exit_program

def create_video(audio_path, text):
    try:
        audio_clip = AudioFileClip(audio_path)
        audio_duration = int(audio_clip.duration)

        fonts = [
            'Cascadia-Code-Regular',
            'Calibri',
            'Lucida-Sans-Regular',
        ]

        font_colors = [
            '#FDFDFD',
            '#2F2F2F',
            '#474543',
        ]
        
        bg_colors = [
            '#A846A0', 
            '#6866C6',
            '#23CE6B'
        ]
        
        the_size = (900, 600)
        
        txtClip = TextClip(text, 
                           color=font_colors[0], 
                           font=fonts[2], 
                           fontsize=112, 
                           bg_color=bg_colors[0],
                           size=the_size, 
                           method='caption', 
                           align='center')

        cvc = CompositeVideoClip(
            [txtClip], #.set_pos('center') 
            size=the_size).set_duration(audio_duration)

        output_path = f'test/video2.mp4'

        # cvc.set_audio(audio_clip).volumex(2).write_videofile(output_path, fps=25)
        cvc.set_audio(audio_clip).write_videofile(output_path, fps=25)
        print('Successfully ran script')
        
    except Exception as ex:
        print(f'An exception occcurred - ex:\n{ex.__str__}')
    finally:
        exit_program() 

'''
    The script can be stopped by: 
    KeyboardInterrupt exception. ie ctrl + c .
'''
try:
    create_video(
        audio_path='data/audio/phrases/at_the_edge_of_the_cliff.wav', 
        text='At the edge of the cliff')
                
except KeyboardInterrupt:
    exit_program()
    print('\nEnding script.. gracefully')
finally:
    print('Ending script.')
    exit_program()
    