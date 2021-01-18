import pywhatkit 
from speak import speak
import wikipedia
from cleantext import clean
import re


def searchgoogle(query):
    '''indx = query.split().index("search") 
    #indx = query.split().index("google")
    query = query.split()[indx + 1:] '''
    query = query.replace("search", "")
    query = query.replace("google", "")
    try: 
        print("Searching for "+ query) 
        speak("Searching for "+ query)
        speak("Here is the result : ")
        pywhatkit.search(query)

    except Exception as e:
        print(e)
        print("Sorry, An Unknown Error Occured. Please try again")
        speak("Sorry, An Unknown Error Occured. Please try again")

def whois(query):
    query = query.replace("who is", "")
    query = query.replace("who was", "")
    
    try: 
        print("Searching for "+ query) 
        speak("Searching for "+ query)
        print("Here is the result : ")
        res1 = pywhatkit.info(query, lines = 2)
        #result = re.sub(r'\([^)]*\)', '', res1)
        result = clean(res1)
        speak("Here is the result : ")
        print(result)
        speak(result)

    except Exception as e:
        print(e)
        print("Sorry, An Unknown Error Occured. Please try again")
        speak("Sorry, An Unknown Error Occured. Please try again")

def searchyt(query):
    query = query.replace("search", "",1)
    query = query.replace("youtube", "",1)
    query = query.replace("play", "",1)
    try: 
        if "search" in query:
            print("Searching for "+ query+ " on youtube") 
            speak("Searching for "+ query+ " on youtube")
        elif "play" in query:
            print("Playing "+ query) 
            speak("Playing "+ query)
        pywhatkit.playonyt(query) 

    except Exception as e:
        print(e)
        print("Sorry, An Unknown Error Occured. Please try again")
        speak("Sorry, An Unknown Error Occured. Please try again")
        
def wiki(query):
    query = query.replace("search", "",1)
    query = query.replace("wikipedia", "",1)
    try: 
        print("Searching for "+ query+ " on wikipedia")
        speak("Searching for "+ query+ " on wikipedia")
        res1 = wikipedia.summary(query, 2)
        result = re.sub(r'\([^)]*\)', '', res1)
        #result = clean(res1)
        print(result)
        speak(result)

    except Exception as e:
        print(e)
        print("Sorry, An Unknown Error Occured. Please try again")
        speak("Sorry, An Unknown Error Occured. Please try again")

def playsong(query):
    query = query.replace("play", "",1)
    try: 
        print("Playing"+ query)
        speak("Playing"+ query)
        pywhatkit.playonyt(query)

    except Exception as e:
        print(e)
        print("Sorry, An Unknown Error Occured. Please try again")
        speak("Sorry, An Unknown Error Occured. Please try again")


'''from selenium import webdriver
from speak import speak
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def search(query):   
    driver = webdriver.Edge()
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    browser.implicitly_wait(1) 
    browser.maximize_window(True)
    query = "Search Wikipedia Dhoni"
    try:
        words = ['youtube', 'google', 'wikipedia', 'search']
        indx = query.lower.split().index(any(words))
        query = query.split()[indx + 1:]  
        if 'youtube' in query: 
            speak("Opening in youtube") 
            driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
            return
    
        elif 'wikipedia' in query: 
    
                speak("Opening Wikipedia") 
                driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
                return
    
        else: 
    
            if 'google' in query: 
                driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
    
            elif 'search' in query: 
                driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
    
            else: 
                driver.get("https://www.google.com/search?q =" + '+'.join(query.split())) 
    
            return
        
    except Exception as e:
            print(e)
            print("Please, Say that again sir")
            #speak("Please, Say that again sir")
            return "None"
'''