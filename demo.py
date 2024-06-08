import os
import speech_recognition as sr
import pyttsx3 
import datetime
import webbrowser

recogniz = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recogniz.adjust_for_ambient_noise(source)
        audio = recogniz.listen(source)
    try:
        command = recogniz.recognize_google(audio).lower()
        print("you said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, Could not understand the audio.") 
    except sr.RequestError:
        print("Sorry, Could not process the request.Try again later.")

def main():
    while True:
        command = listen()

        if "hello" in command:
            speak("Hey there! How can i assist you?")
        elif "how are you" in command:
            speak("I'm just a computer program, but thank you for asking.If i can help with anything,just ask.")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{current_time}.")
            print("time")
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%D-%m-%Y")
            speak(f"The date is {current_date}.")
            print("date")
        elif "open youtube" in command:
            speak("Ok! Opening youtube.")
            print("open youtube")
            webbrowser.open("youtube.com")
        elif "open google" in command:
            speak("Ok! Opening google.")
            print("open google")
            webbrowser.open("google.com")
        elif "play music" in command:
            speak("Here you go! Opening spotify.")
            print("play music")
            webbrowser.open("spotify.com")
        elif "search" in command:
            query = command.split("search", 1)[1].strip()
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for other web {query}.")
            webbrowser.open(url)
        elif "exit" in command:
            speak("Goodbye! Have agreat day!")
            print("exit")
            break
        else:
            speak("Sorry, I didn't catch that. Can you please repeat?")
            continue
if __name__ == "__main__":
    main()


    
