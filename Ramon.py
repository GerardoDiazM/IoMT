import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say('Hola... Soy Ramón')
engine.say('¿Qué puedo hacer por ti?')
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'Ramón' in command:
            print(command)
except:
    pass