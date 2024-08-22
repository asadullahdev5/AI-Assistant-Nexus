import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui

""
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')       
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
    speak("Please tell me. What can I do for you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Wait for a few moments")
            query = r.recognize_google(audio, language="en-in")
            print(f"You just said: {query}\n")
        except Exception as e:
            print(e)
            speak("Please tell me again")
            query = "none"
        return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            wishMe()
            while True:
                query = takeCommand().lower()

                # Time teller
                if "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                # Browsers callback conditions command
                elif "linkedin" in query or "open my linkedin account" in query:
                    speak("Opening LinkedIn...")
                    os.startfile(
                        "https://www.linkedin.com/in/asad-ullah-553b152b3?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
                    )

                elif "github" in query or "open my github account" in query:
                    speak("Opening Github...")
                    os.startfile("https://github.com/AsadDev09")

                elif "brave" in query and "search on brave" in query:
                    speak("Opening Brave...")
                    os.startfile(
                        "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                    )

                # Search on browser
                elif "open" in query or "search" in query:
                    query = query.replace("open", "")
                    pywhatkit.search(query)
                    speak("Done, Sir!")

                elif "wikipedia" in query:
                    speak("Opening Wikipedia...")
                    try:
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except:
                        speak("No result found")
                        print("No result found")

                elif "play" in query:
                    query = query.replace("play", "")
                    speak(f"Playing {query}")
                    pywhatkit.playonyt(query)

                elif "type" in query:
                    speak("What should I write?")
                    while True:
                        writeInNotepad = takeCommand()
                        if writeInNotepad == "exit typing":
                            speak("Done, Sir")
                            break
                        else:
                            pyautogui.write(writeInNotepad)

                elif "exit" in query:
                    speak("It's my pleasure to assist you..")
                    speak("Now I'm leaving!")
                    quit()

                elif "break" in query:
                    speak("Thanks, Sir!")
                    break

                # Interaction commands
                elif "how are you" in query:
                    speak("I'm fine, thanks for asking..")
                    speak("How can I help you?")

                elif "who are you" in query or "hu r u" in query:
                    speak("I'm a virtual assistant")
                    speak("Created by you using Python")

                elif "what is your name" in query or "what's your name" in query:
                    speak("My name is Nexus")
                    speak("How can I help you?")

                elif (
                    "its incorrect" in query
                    or "it's incorrect" in query
                    or "glOat hai" in query
                    or "its wrong" in query
                ):
                    speak("Sorry, Sir.")

                elif (
                    "thanks" in query
                    or "cool" in query
                    or "thats nice" in query
                    or "good job" in query
                ):
                    speak("It's my pleasure")
                    ""
        else:
            print("I'm sleeping")
