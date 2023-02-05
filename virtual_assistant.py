#To recognise speech
import speech_recognition as sr 
#To play an audio
import playsound
import random
#Google Text to speech
from gtts import gTTs 
#To open web-browser
import webbrowser
import ssl
import certifi
import time 
#To remove the audio files
import os
import subprocess
from PIL import Image
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request

class person:
    name=''
    def setName(self.name):
        self.name = name

class asis:
    name=''
    def setName(self.name):
        self.name=name

def there_exists(terms):
    for term in terms:
        if term in value_date:
            return True

def engine_speak(text):
    text=str(text)
    engine.say(text)
    engine.runAndWait()

#To initialize the recognizer
#It is used to listen the audio and convert it into text
r=sr.Recognizer()

def record_audio(ask=""):
    #Defining Microphone as source to receive audio as input
    with sr.Microphone() as source:
        if ask: 
            engine_speak(ask)
        #To listen audio via source i.e. microphone 
        audio=r.listen(source, 5, 5)
        print("Done Listening")
        voice_data=""
        try:
            #To convert audio into text
            voice_data=r.recognise_google(audio)
        
        #To except the error when the recogniser is not able to understand the input
        except sr.UnkonwnValueError:
            engine_speak("Sorry sir, I didn't get that")
        #To except the error when the reconizer is not connected to the internet
        except sr.RequestError:
            engine_speak("Sorry No internet connection")
            #To print what the user input
            print(">>",voice_data.lower())
            return voice_data.lower()

#To convert the text into speech which will be spoken by our assistant i.e engine
def engine_speak(audio_string):
    audio_string=str(audio_string):
    #Text to Speech
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,20000000)
    audio_file=
     

