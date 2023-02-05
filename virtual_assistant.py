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
    audio_file='audio' + str(r) + '.mp3'
    #To save converted text into audio in mp3 form
    tts.save(audio_file)
    #To play the audio which is actually the voice of our assistant
    playsound.playsound(audio_file)
    #To print what our assistant said
    print(asis_obj.name+ ":",audio_string)
    #To remove the file
    os.remove(audio_file)

def respond(voice_data):
    #1) Greetings
    if there_exists(["hello","hi","hey","hey boss","hola"]):
        greetings=['Hey, how can I help you ?'+person_obj.name, 'How can I help you ?'+person_obj.name, 'Hello'+person_obj.name]
        greet=greetings[random.randint(0,length(greetings)-1)]
        engine_speak(greet)

    #2) Name
    if there_exists(["What is your name?","Tell me your name.."]):
        if person_obj.name:
            engine_speak("I don't know my name, please give me my name by saying command your name should be......what is your name ")
        else: 
            engine_speak("What's your name sir/ma'am ?")

    if there_exists(["My name is"]):
        person_name=voice_data.split("is")[-1].strip()
        engine_speak("Okay Sir/Ma'am I'll remember that your name is"+person_name())
        person_obj.setName(person_name)

    if there_exists(["Your name should be"]):
        asis_name=voice_data.split('be')[-1].strip()
        engine_speak("Okay, I'll remember that my name is"+asis_name())
        asis_obj.setName(asis_name) #Remembering the given name

    #3) Greetings 
    if there_exists(["How are you ?","How are you doing ?"]):
        engine_speak("I'm very well! Thanks for asking"+person_obj.name)

    #4)Time 
    if there_exists(["Whats the time?","Tell me the Time.."]):
        time=ctime().split(" ")[3].split(":")[0:2]
        if time[0]=="00":
            hours='12'
        else:
            hours=time[0]
            minutes=time[1]
            time=hours+' hours and '+minutes+" minutes"
            engine_speak(time)

    #5)Searching
    if there_exists(["Search for"]) and 'Youtube' not in voice_data:
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q"+search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for "+search_term+" on google")

    #6)Open youtube and search
    if there_exists(["youtube"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.youtube.com/results?search_query="+search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for "+search_term+" on youtube")

    #7)To Know the Stock Price
    if there_exists(["price of "]):
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q"+search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for "+search_term+" on google")

    #Search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to "+ search_term +" enjoy sir/ma'am")

    #Search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for "+search_term + " on amazon.com")
         
    #make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here's where you can make notes...")
        
    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("Opening Instagram")
        
    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("Opening Twitter")
        
    #8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\AI and ml project\Virtual Assistant\VI sem- CSE.docx")
        im.show()
    
    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for "+search_term+" on google")
    
    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("Here's where you can check your gmail")   

    #10 stone paper scisorrs
    
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
    #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/YASH/Pictures/Screenshots') 
    
    
    #14 Search on wikipedia
    if there_exists(["definition of"]):
        definition=record_audio("What do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('I\'m sorry I could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('Here is what I found '+definitions[1])
            else:
                engine_speak ('Here is what I found '+definitions[2])
        else:
                engine_speak("I'm sorry I could not find the definition for "+definition)


    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("we could continue more sir, but.,,...,,,,,..,,,,, byee")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Kim'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond 
