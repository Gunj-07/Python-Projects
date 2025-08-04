import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    while True:
        recongizer = sr.Recognizer()
        with sr.Microphone() as source:
            print(" Listening...\nSpeak Now... ")
            recongizer.adjust_for_ambient_noise(source)
            audio = recongizer.listen(source)
            try:
                print("Recognizing...")
                data = recongizer.recognize_google(audio)
                print(data) 
                return data
            except sr.UnknownValueError:
                print(" Not understanding...\nTry Again... ")

def speechtx(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":

    if  "hello don" in sptext().lower():
        speechtx("Yes,speak now")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "My name is Don"
                speechtx(name)
            elif "your age" in data1:
                age = "im 10 yaers old"
                speechtx(age)
            elif "current time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "google" in data1:
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                joke1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke1)
                speechtx(joke1)
            elif "whatapp" in data1:
                os.system("WhatsApp")
            elif "open photo" in data1:
                add = "D:\wallpaper"
                photolist = os.listdir(add)
                print(photolist)
                data2 = sptext().lower()
                if "avengers" in data2:
                    os.startfile(os.path.join(add,photolist[0]))
                elif "code" in data2:
                    os.startfile(os.path.join(add,photolist[1]))
                elif "cricket" in data2:
                    os.startfile(os.path.join(add,photolist[2]))
                elif "iron man" in data2:
                    os.startfile(os.path.join(add,photolist[3]))
                elif "iron man 1" in data2:
                    os.startfile(os.path.join(add,photolist[4]))
                elif "iron man 2" in data2:
                    os.startfile(os.path.join(add,photolist[5]))
                elif "iron man 3" in data2:
                    os.startfile(os.path.join(add,photolist[6]))
                elif "spider-man" in data2:
                    os.startfile(os.path.join(add,photolist[7]))
                elif "thor" in data2:
                    os.startfile(os.path.join(add,photolist[8]))
                elif "thor 1" in data2:
                    os.startfile(os.path.join(add,photolist[9]))
                else:
                    speechtx("Image not found")
            elif "exit" in data1:
                speechtx("Okay,Thank You!!! Byeeeeeeeee")
                break
            time.sleep(3)
    else:
        speechtx("Not recognised")