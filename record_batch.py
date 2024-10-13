'''
        This script listens for audio input when the space bar is pressed and stops recording when the space bar is released.
    It uses the SpeechRecognition library to transcribe the audio and saves the recognized text along with the recorded audio.
    
    Key Features:
    - The program waits for the user to press and hold the space bar to begin recording audio.
    - When the space bar is released, the recording stops, and the audio is processed.
    - The transcribed text from the recording is saved to a text file (words.txt), along with the path to the saved audio file.
    - Audio recordings are saved in WAV format in the 'audio' directory, creating the directory if it doesn't exist.
    - The script logs errors and relevant events to 'assets/record_batch.log' for debugging.
    - The program continuously listens for space bar events until manually interrupted (Ctrl+C).
'''

import speech_recognition as sr
import pyttsx3
import logging
import keyboard
import time
import os

# Configure logging
logging.basicConfig(filename='assets/record_batch.log', 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

r = sr.Recognizer()

def record_text():
    try:
        # Check if a microphone is available
        with sr.Microphone() as source2:
            # Adjusts for ambient noise
            r.adjust_for_ambient_noise(source=source2, duration=0.2)  
            print('Recording...')
            
            # Captures the audio while space bar is held down
            audio2 = r.listen(source2)  

            # Recognize the audio using Google Speech Recognition
            text_data = r.recognize_google(audio2)
            
            # Optional: Convert the text to lowercase
            text_data = text_data.lower()
            
            # Save the audio:
            audio_file_path = os.path.join('new-audios', f'{text_data}.wav')
            
            # if path DNE, create it:
            if not os.path.exists('audio'):
                os.makedirs('audio')
            
            with open(audio_file_path, 'wb') as f:
                f.write(audio2.get_wav_data())
                
            print('You said: ', text_data)
            print('Saved audio recording: ', audio_file_path)
            return text_data, audio_file_path
        
    except AssertionError as e:
        logging.error('AssertionError')
        print(f'Microphone access error: {e}')
    except sr.RequestError as e:
        logging.error('RequestError')
        print('Could not request results from Google Speech Recognition service; {0}'.format(e))
    except sr.UnknownValueError:
        logging.error('UnknownError')
        print('Google Speech Recognition could not understand the audio')

    # Return an empty string only if no valid text is recognized
    return '', ''

def output_text(text, audio_path):
    # Only write non-empty text
    if text:  
        with open('words.txt', 'a') as f:
            f.write(f'{text} ({audio_path})')
            f.write('\n')
    return

# Main loop
try:
    print("Waiting to start... Press and hold space bar to record.")
    
    while True:
        # Wait until the space bar is pressed
        if keyboard.is_pressed('space'):
            start_time = time.time()
            
            # Start recording when space is pressed
            text, audio_path = record_text()
            
            # Stop when space is released
            while keyboard.is_pressed('space'):
                pass

            print("Recording stopped")
            
            # Output the recognized text if available
            if text:
                output_text(text, audio_path)
                print('Text successfully written')
                print('Audio file saved successfully')

        time.sleep(0.1)  # To prevent high CPU usage in the loop

except KeyboardInterrupt:
    print('\nProgram interrupted. Exiting gracefully...')
finally:
    print('Program has stopped.')
