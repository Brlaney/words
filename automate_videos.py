import json, io
from moviepy.editor import *

def create_video(audio_path, text_value):
    audio_clip = AudioFileClip(audio_path)

    # Define video dimensions
    screensize = (550, 375)

    # Define the text
    txtClip = TextClip(text_value, 
                       color='white', 
                       font="Ariel", 
                       fontsize=144, 
                       bg_color='black')

    # Create a composite video obj
    cvc = CompositeVideoClip([txtClip.set_pos('center')], size=screensize).set_duration(4)

    # Set the audio to the video
    video = cvc.set_audio(audio_clip)
    
    # Write the output to a new video file
    video.write_videofile(f"videos/{text_value}.mp4", fps=25)

json_obj = {
    "id": 12,
    "text": "aside",
    "path": "audio/aside.wav"
}

# Serializing json
json_object = json.dumps(json_obj, indent=4)

# Extract audio path and text from the JSON object
audio_path = json_obj["path"]
text_value = json_obj["text"]

create_video(audio_path, text_value)