import pyttsx3 
import speech_recognition as sr 
import webbrowser 
import wikipedia 
import os
import sys
import pyjokes
import pywhatkit
from googleapi import google
import searchconsole
import wolframalpha 
from playsound import playsound as ps

from takeCommand import takeCommand
from speak import speak
from search import *
from DayTime import *

    
def hello():
    print("Hey there ! I am  SAYKA, how may I help you ?")
    speak("Hey there ! I am  SAYKA, how may I help you ?")
    
def TakeQuery():
    
    while True:
        query = takeCommand()
        if query == "":
            continue
        else:
            if "open" in query:
                query = query.replace("open", "", 1)
                #query = query.replace("dot com", "", 1)
                query = query.replace(" ","/")
                query = query.strip()
                print("Opening " +query)
                speak("Opening " +query)
                webbrowser.open("http://" +query+".com")
                
                
            if "hello" == query or "hey" in query:
                hello()
                
            if "which day is it today" in query or "today's day" in query:
                tellDay()
            
            if "tell time"  in query or "tell me the time" in query or "what time is it now"  in query or "tell time" in query:
                tellTime()
            
            if "play" in query or "search" and "on youtube" in query:
                searchyt(query)
                
            if "from wikipedia" in query or "wikipedia" in query or "in wikipedia" in query or "search" and "wikipedia" in query:
                wiki(query)
            
            if "search" in query and not "wikipedia" in query or "give me information about" in query:
                query = query.replace("give me information about", "")
                searchgoogle(query)
    
            if "who is" in query or "who was" in query:
                whois(query)
                
            if "tell me" and "joke" in query or "me a joke" in query:
                print("Okay, let me see if I have any, \nHere is a joke ")
                speak("Okay, let me see if I have any, \nHere is a joke ")
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
                #can also perform a tongue twister by changing the category
                
                
            if "tell me your name" in query or "what is your name" in query or "who are you" in query:
                print("My name is SAYKA, your Intelligent Personal Assistant (IPA)")
                speak("My name is SAYKA,  your Intelligent Personal Assistant")
                
            if "bye" in query or "exit" in query  or "stop" in query or "quit" in query or "talk to you later" in query or "see you again" in query or "ciao" in query:
                speak("Exiting. Bye, see you later")
                print("Exiting.")
                print("Bye, see you later")
                ps("exit.mp3")
                sys.exit()
            
            
            '''if("from wikipedia" in query or "check wikipedia" in query or "in wikipedia" in query) and "in hindi" in query:
                print("Checking in wikipedia ")
                speak("Checking in wikipedia ")
                wikipedia.set_lang("hi")
                query = query.replace("in hindi", "",1)
                query = query.replace("wikipedia", "",1)
                result = wikipedia.summary(query, sentences = 1)
                print("According to wikipedia, \n\t",result)
                speak("According to wikipedia")
                speak(result)'''
                
            '''if "who is" in query or "calculate" in query or "who is" in query:
                app_id = "SAYKA" 
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate') 
                query = input.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text 
                speak("The answer is " + answer) 
                return'''
                
            '''if"search" in query or "google" in query:
                print("Searching for your query...")
                speak("Searching")
                query = query.replace("search", "") or query.replace("google", "")
                search_results = google.search(query, 1)
                result = search_results[1].description
                print("Here are the search results \n\t",result)
                #speak("According to google")
                speak(result)
            '''
            '''if "make a note" or "write this down" or "make me a note" in query:
                MakeNote()
                
            if "play music" in query:
                PlayMusic()
            
            if "open"+application in query:
                #code
            
            if "tell me a joke" in query:
                TellJoke()
            
            if "in youtube"
            
            wake word insertion to wake SAYKA'''
            
if __name__ == "__main__":
    TakeQuery()