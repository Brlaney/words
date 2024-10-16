import speech_recognition as sr
import pyttsx3
import logging

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
            print('Listening...')
            
            # Captures the audio
            audio2 = r.listen(source2)  

            # Recognize the audio using Google Speech Recognition
            text_data = r.recognize_google(audio2)
            
            # Optional: Convert the text to lowercase
            text_data = text_data.lower()  
            
            # Check if the recognized text is 'exit' or 'stop'
            if text_data in ['exit', 'stop']:
                print('Exit command received, stopping the program.')
                return text_data  # Return the exit command to stop the loop
            
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
        with open('words.txt', 'a') as f:
            f.write(text)
            f.write('\n')
    return

# Main loop
try:
    while True:
        # Record speech and convert to text
        text = record_text()  
        
        # Check for exit or stop command to end program
        if text in ['exit', 'stop']:  
            break  
        
        # Only output non-empty text
        if text:  
            output_text(text)
            print('Text successfully written')
            
except KeyboardInterrupt:
    print('\nProgram interrupted. Exiting gracefully...')
finally:
    print('Program has stopped.')