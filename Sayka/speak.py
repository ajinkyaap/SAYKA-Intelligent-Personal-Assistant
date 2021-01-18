import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #for female voice
    #engine.setProperty('voice', voices[0].id) for male voice
    engine.say(audio)
    
    engine.runAndWait()