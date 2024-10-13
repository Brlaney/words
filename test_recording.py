import speech_recognition as sr
import pyttsx3
import logging
import keyboard
import time

# Configure logging
logging.basicConfig(filename='assets/audio_to_text.log', 
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
            
            print('You said: ', text_data)
            return text_data
        
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
    return ''

def output_text(text):
    # Only write non-empty text
    if text:
        with open('words2.txt', 'a') as f:
            f.write(text)
            f.write('\n')

# Main loop
try:
    print("Waiting to start... Press and hold space bar to record.")
    
    while True:
        # Wait until the space bar is pressed
        if keyboard.is_pressed('space'):
            start_time = time.time()
            
            # Start recording when space is pressed
            text = record_text()
            
            # Stop when space is released
            while keyboard.is_pressed('space'):
                pass

            print("Recording stopped")
            
            # Output the recognized text if available
            if text:
                output_text(text)
                print('Text successfully written')

        time.sleep(0.1)  # To prevent high CPU usage in the loop

except KeyboardInterrupt:
    print('\nProgram interrupted. Exiting gracefully...')
finally:
    print('Program has stopped.')
