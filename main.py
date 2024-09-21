import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import requests
from bs4 import BeautifulSoup
import wikipedia
import subprocess
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Flag to check if Jarvis is processing a command
processing = False

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    global processing  # Access the global flag
    processing = True  # Start processing the command

    # Show a message to indicate processing
    print("Processing...")

    # File Management Commands
    if "open file" in c.lower():
        filename = c.lower().split("open file ")[1]
        if os.path.exists(filename):
            os.startfile(filename)
            speak(f"Opening {filename}")
        else:
            speak(f"File {filename} not found.")
    
    # Weather Updates Using Web Scraping
    elif "weather" in c.lower():
        city = c.lower().split("weather in ")[1]
        get_weather(city)
    
    # Task Automation (Opening Apps or Setting Reminders)
    elif "open notepad" in c.lower():
        subprocess.Popen(["notepad.exe"])
        speak("Opening Notepad")
    
    elif "set reminder" in c.lower():
        reminder = c.lower().split("set reminder ")[1]
        with open("reminders.txt", "a") as file:
            file.write(reminder + "\n")
        speak(f"Reminder set: {reminder}")
    
    # Wikipedia Integration (Using Web Scraping)
    elif "wikipedia" in c.lower():
        query = c.lower().replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything on that topic.")
    
    # General Web Commands
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    else:
        speak("Sorry, I didn't understand the command.")

    processing = False  # Command has been processed

# Function to get weather information
def get_weather(city):
    try:
        r = requests.get(f"https://www.weather-forecast.com/locations/{city}/forecasts/latest")
        soup = BeautifulSoup(r.text, 'html.parser')
        weather = soup.find("span", class_="phrase").text
        speak(f"The current weather in {city} is: {weather}")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather information.")

if __name__ == "__main__":
    speak("Initializing Jarvis... ")
    while True:
        if not processing:  # Only listen when not processing a command
            print("Recognizing... Please say 'Jarvis' to activate.")
            try:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                    print("Listening...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yeah, what can I do for you?")
                    print("Jarvis is ready, listening for your command...")
                    # Listen for command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)
                        print("Processing command... Please wait.")
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
            except sr.UnknownValueError:
                # Instead of speaking during processing, print this message for debugging.
                if not processing:
                    print("Sorry, I didn't catch that. Please try again.")
            except sr.RequestError as e:
                speak(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error: {e}")
