#Speech to speech conversion

import pyttsx3
import speech_recognition as sr

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something....")
        audio = r.listen(source)
        print("done!")
        
    try:
        text = r.recognize_google(audio)
        text_to_speech(text)
        
    except Exception as e:
        print(e)
    

def text_to_speech(data):
    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()

speechtotext()