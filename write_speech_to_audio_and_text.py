import speech_recognition as sr
from pydub import AudioSegment
import os, logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
r = sr.Recognizer()

def record_text():
    try:
        # Check if a microphone is available
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)  # Adjusts for ambient noise
            # logging.debug(f"Ambient noise adjusted in {time.time() - start_time} seconds")
            print("Listening...")
            # Captures the audio
            audio2 = r.listen(source2)  
            # logging.debug(f"Audio captured in {time.time() - start_time} seconds")
            
            # Recognize the audio using Google Speech Recognition
            text_data = r.recognize_google(audio2)
            # Convert the text to lowercase
            text_data = text_data.lower()

            # Save the audio
            audio_file_path = os.path.join("audio", f"{text_data}.wav")
            if not os.path.exists("audio"):
                os.makedirs("audio")
            with open(audio_file_path, "wb") as f:
                f.write(audio2.get_wav_data())
            
            # logging.debug(f"Audio saved in {time.time() - start_time} seconds")
            
            return text_data, audio_file_path

    except AssertionError as e:
        logging.error(f"Microphone access error: {e}")
    except sr.RequestError as e:
        logging.error(f"Request error: {e}")
    except sr.UnknownValueError:
        logging.error("Unknown value error")

    return "", ""

def output_text(text, audio_path):
    # Only write non-empty text
    if text:  
        with open("output.txt", "a") as f:
            f.write(f"{text} ({audio_path})")
            f.write("\n")
    return

# Main loop
while True:
    # Record speech and convert to text
    text, audio_path = record_text()
    
    # Exit the loop gracefully
    if text in ["exit", "stop"]:
        break  

    # Only output non-empty text
    if text:
        output_text(text, audio_path)
        print(f"Text: '{text}' and audio recorded at '{audio_path}' successfully written")

print("Program has stopped.")
