import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import random
import requests
import wikipedia
import os
import datetime
import g4f
import pyjokes
import smtplib
import subprocess
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Capture and recognize speech"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, speech recognition service is unavailable.")
        return None

def get_weather(city="New Delhi"):
    """Fetch real-time weather data for a given city"""
    API_KEY = "1e8bd439beea3af25723412410eee3df"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(URL)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"]
            return f"The temperature in {city} is {temp}°C with {weather_desc}."
        else:
            return "Sorry, I couldn't fetch the weather data."
    except:
        return "Unable to fetch weather information."

def tell_joke():
    """Tell a random joke using the pyjokes module"""
    return pyjokes.get_joke()

def change_volume(level):
    """Adjust system volume"""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    speak(f"Volume set to {level} percent.")

def change_brightness(level):
    """Adjust monitor brightness"""
    sbc.set_brightness(level)
    speak(f"Brightness set to {level} percent.")

def small_talk(command):
    """Handle basic conversation responses"""
    responses = {
        "how are you": "I'm just a virtual assistant, but I'm feeling great! How about you?",
        "how do you feel": "I don't have emotions, but I'm happy to assist you!",
        "what's your name": "I'm R2D2, your AI assistant!",
        "who created you": "I was created by a developer who wanted to make life easier!",
        "what do you do": "I can chat, tell jokes, provide weather updates, search the web, and more!",
        "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
        "do you sleep": "I don't need sleep, but I do take small breaks!",
        "what's your favorite color": "I like all colors equally, but blue seems calming!",
        "what's your favorite movie": "I don't watch movies, but I've heard Inception is pretty mind-blowing!",
        "can you be my friend": "Of course! I'm here to assist and chat with you anytime!"
    }
    for key in responses:
        if key in command:
            return responses[key]
    return None

def ai_response(query):
    """Get response from g4f AI model"""
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": query}]
        )
        return response
    except:
        return "I'm unable to process that request at the moment."

def open_application(command):
    """Open common applications"""
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "spotify": "C:\\Users\\athar\\AppData\\Roaming\\Spotify\\Spotify.exe"
    }
    for app in apps:
        if app in command:
            subprocess.Popen(apps[app])
            speak(f"Opening {app}.")
            return
    speak("Sorry, I couldn't find that application.")

def ai_assistant():
    """Main AI assistant loop"""
    speak("Hello! Say 'assistant' to activate me.")
    
    while True:
        command = recognize_speech()
        if command is None:
            continue
        
        if "assistant" in command:
            speak("Yes, how can I help you?")
            
            while True:
                command = recognize_speech()
                if command is None:
                    continue
                
                if "time" in command:
                    speak(f"The time is {time.strftime('%I:%M %p')}")
                elif "date" in command:
                    speak(f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}")
                elif "open" in command:
                    open_application(command)
                elif "weather" in command:
                    speak("Which city do you want the weather for?")
                    city = recognize_speech()
                    if city:
                        speak(get_weather(city))
                elif "joke" in command:
                    speak(tell_joke())
                elif "volume" in command:
                    speak("What volume level do you want?")
                    level = recognize_speech()
                    if level and level.isdigit():
                        change_volume(int(level))
                elif "brightness" in command:
                    speak("What brightness level do you want?")
                    level = recognize_speech()
                    if level and level.isdigit():
                        change_brightness(int(level))
                elif "wikipedia" in command:
                    speak("What do you want to search on Wikipedia?")
                    query = recognize_speech()
                    if query:
                        speak(wikipedia.summary(query, sentences=2))
                elif "search" in command:
                    speak("What do you want to search for?")
                    query = recognize_speech()
                    if query:
                        webbrowser.open(f"https://www.google.com/search?q={query}")
                        speak(f"Searching Google for {query}")
                elif "exit" in command or "stop" in command or "goodbye" in command:
                    speak("Goodbye! Have a great day.")
                    return
                else:
                    small_talk_response = small_talk(command)
                    if small_talk_response:
                        speak(small_talk_response)
                    else:
                        ai_reply = ai_response(command)
                        speak(ai_reply)

# Run the assistant
ai_assistant()