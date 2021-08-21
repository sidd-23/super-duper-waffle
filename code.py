import pyttsx3 #text to speech module
import speech_recognition as sr  #speech recognition module
import datetime
import wikipedia
import webbrowser
import os
import sys
import smtplib
MASTER = "mister creed"
print("Initializing Diana...")
engine = pyttsx3.init('sapi5') #sapi5 is the microsoft speech technology for voice recognition
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(text): #this speak function will pronounce the string
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour) #current date time usingdate time module

    if hour>=0 and hour<12:
        speak("good morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)
    elif hour>=18 and hour<24:
        speak("good evening" + MASTER)
    speak("how may i help you Sir!?")


def time_info():
    time = datetime.datetime.now()

    if 'what is the time' in query.lower():
        speak('Current time is %d hours %d minutes' % (time.hour, time.minute) + 'Sir')

#recieving commands
def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source :
         print("Listening...")
         audio = r.listen(source , phrase_time_limit= 5)
     try:
          print("Recognizing...")
          query = r.recognize_google(audio, language='en-in')
          print(f"Mr.Creed said: {query}\n")

     except sr.UnknownValueError :
          print("Pardon me Sir ! can you say that again ?")
          query = takecommand();

     return query


speak("Initializing Diana ...")
wishme()
query = takecommand()
time_info()



if 'wikipedia' in query.lower():
    speak('Searching wikipedia ...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query , sentences=2)
    speak(results)

elif 'open youtube' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url="youtube.com")

elif 'open google' in query.lower() or 'search' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url="google.com")

elif 'open facebook' in query.lower() or 'f b'in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url="facebook.com")

elif 'open instagram' in query.lower() or 'insta' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url="instagram.com")

elif 'open whatsapp' in query.lower():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url="web.whatsapp.com")

elif 'good bye' in query.lower() or 'no thank you' in query.lower() or 'take rest' in query.lower():
    speak('Bye Mr.creed ! call me back when you need')
    sys.exit()



