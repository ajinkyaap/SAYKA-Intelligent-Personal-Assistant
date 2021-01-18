import speech_recognition as sr 
from speak import speak
from playsound import playsound as ps

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        ps('start.mp3')
        print("Listening...")
        
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source,duration = 0.25)
        audio = r.listen(source)
        
        try :
            print("Recognizing...")
            
            Query = r.recognize_google(audio, language = "en-in")
            print("You said : " + Query)
        
        except Exception as e:
            print(e)
            print("Please, Say that again sir")
            speak("Please, Say that again sir")
            return ""
        
    return Query.lower()
