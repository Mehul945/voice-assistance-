import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import webbrowser
import os
import random
import re
# import pyaudio
# import wikipedia #pip install wikipedia
# import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" I am Heer. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.adjust_for_ambient_noise(source,duration=4)
        audio = r.listen(source)
    try:
        # query=''
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


exit = ['exit', 'exit heer', 'quit heer', 'quit', 'stop heer', 'stop']
time = ['what is the time', 'what is time',
        'heer time kya hua hai', 'time kya hua hai', 'time kya hua hai heer', "time su thayo che", 'ketala vagya', 'heer ketala vagya', 'ketala vagya heer', ]
if __name__ == "__main__":
    wishMe()
    A = True
    while A:
        query = takeCommand().lower()
        if 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'hey google' in query:
            search = query[11:]
            if search=='':
                pass
            else:
                print("searching On Google...")
                webbrowser.open_new("https://www.google.com/search?q="+search)
            
        elif 'hey youtube' in query:            
            search = query[11:]
            if search=='':
                pass
            else:
                print("searching On YouTube...")
                search = query[12:]
                webbrowser.open("https://www.youtube.com/results?search_query="+search)
        elif 'hey youtube play video' in query:            
            search = query[22:]
            if search=='':
                pass
            else:
                speak("playing On YouTube..."+search)
                search = query[12:]
                webbrowser.open("https://www.youtube.com/results?search_query="+search)
        elif 'play music' in query:
            path = "C:/Users/mehul/Music"
            Music = os.listdir(path)
            lensong = len(Music)
            no = query.index('play music')
            search1 = query[(no+11):].lower()
            search2 = query[:no].lower()
            for i in range(lensong):
                # print(songs[i].lower())
                if search1 in Music[i].lower().replace('_', " "):
                    os.startfile(os.path.join(path, Music[i]))
                    print(Music[i].replace('_', ' '))
                    speak('enjoy the Music ')
                elif search2 in Music[i].lower().replace('_', " "):
                    os.startfile(os.path.join(path, Music[i]))
                    print(Music[i].replace('_', ' '))
                    speak('enjoy the music ')

        elif 'play video' in query:
            path = 'C:/Users/mehul/Videos'
            videos = os.listdir(path)
            lensong = len(videos)
            no = query.index('play video')
            search1 = query[(no+11):].lower()
            search2 = query[:no].lower()
            for i in range(lensong):
                # print(songs[i].lower())
                if search1 in videos[i].lower().replace('_', " "):
                    os.startfile(os.path.join(path, videos[i]))
                    print(videos[i].replace('_', ' '))
                    speak('enjoy the video ')
                elif search2 in videos[i].lower().replace('_', " "):
                    os.startfile(os.path.join(path, videos[i]))
                    print(videos[i].replace('_', ' '))
                    speak('enjoy the video ')
        elif "photos" in query:
            path = "C:/Users/mehul/Pictures/Screenshots"
            photos = os.listdir(path)
            os.startfile(os.path.join(path, photos[1]))

        elif query in time:
            hour = datetime.datetime.now().strftime("%I")
            minut = datetime.datetime.now().strftime("%M")
            speak(f"Sir, the time is {int(hour)} hour {int(minut)} minut")
        elif 'open code' in query:
            speak("opening code")
            codePath = "C:/Users/mehul/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(codePath)
        elif 'open adobe' in query:
            speak("opening adobe")
            path = "C:/Program Files (x86)/Adobe/Reader 10.0/ReaderAcroRd32.exe"
            os.startfile(path)
        elif query in exit:
            speak('have a nice day!!!')
            A = False
        elif 'divided by' in query:
            try:
                ia = query.index('divided by')
                print(
                    f"{query[:ia]}/{query[(ia+11):]}= {float(query[:ia])/float(query[(ia+11):])} ")
                speak(
                    f"{query[:ia]} divided by {query[(ia+11):]} is equal to {float(query[:ia])/float(query[(ia+11):])} ")
            except ZeroDivisionError:
                speak(
                    f"{query[:ia]} divided by {query[(ia+11):]} is equal to infinity ")
            except Exception:
                pass

        elif 'x' in query:
            try:
                ia = query.index('x')
                print(
                    f"{query[:ia]}x{query[(ia+1):]}= {float(query[:ia])*float(query[(ia+1):])} ")
                speak(
                    f"{query[:ia]} multiply by {query[(ia+1):]} is equal to {float(query[:ia])*float(query[(ia+1):])} ")
            except Exception:
                pass
        elif '-' in query:
            try:
                ia = query.index('-')
                print(
                    f"{query[:ia]} - {query[(ia+1):]} = {float(query[:ia])-float(query[(ia+1):])}")
                speak(
                    f"{query[:ia]} minus {query[(ia+1):]} is equal to {float(query[:ia])-float(query[(ia+1):])} ")
            except Exception:
                pass
        elif "+" in query:
            try:
                ia = query.index('+')
                print(
                    f"{query[:ia]} + {query[(ia+1):]} = {float(query[:ia])+float(query[(ia+1):])}")
                speak(
                    f"{query[:ia]} plus {query[(ia+1):]} is equal to {float(query[:ia])+float(query[(ia+1):])} ")
            except Exception:
                pass

        # elif query!="open adobe"|query!="open youtube"|query!="open code"|query!="what is the time"|query!="play music"|query!="open stackoverflow"|query!="hey youtube"|query!="hey google"|query!="what is the time":
            # speak("searching on google")
            # webbrowser.open_new("https://www.google.com/search?q="+query)
