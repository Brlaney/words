import json
from moviepy.editor import *
 
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

# Load the audio file using the extracted path
audio_clip = AudioFileClip(audio_path)

# Load the video clip and define the subclip duration
video = VideoFileClip("myHolidays.mp4").subclip(50, 60)

# Overlay text from the JSON object
txt_clip = (TextClip(text_value, fontsize=70, color='white', bg_color='black')
            .set_position('center')
            .set_duration(10))

# Set the audio to the video
video = video.set_audio(audio_clip)

# Combine the video and text clip
result = CompositeVideoClip([video, txt_clip])

# Write the output to a new video file
result.write_videofile("test.mp4", fps=25)