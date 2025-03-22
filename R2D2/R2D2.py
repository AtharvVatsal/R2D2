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
import platform
import psutil
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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
    API_KEY = "YOUR_API_KEY"
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

reminders = {}

def set_reminder():
    """Set a reminder for a specific time"""
    speak("What should I remind you about?")
    reminder_text = recognize_speech()
    if reminder_text:
        speak("When should I remind you? Please specify the time.")
        reminder_time = recognize_speech()
        if reminder_time:
            # This is a simple implementation - could be enhanced with better time parsing
            reminders[reminder_time] = reminder_text
            speak(f"I'll remind you to {reminder_text} at {reminder_time}")

def check_reminders():
    """Check if there are any reminders for the current time"""
    current_time = time.strftime('%I:%M %p')
    if current_time in reminders:
        speak(f"Reminder: {reminders[current_time]}")
        del reminders[current_time]

def get_news():
    """Fetch and read top news headlines"""
    NEWS_API_KEY = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url)
        news = response.json()
        speak("Here are today's top headlines:")
        for i, article in enumerate(news['articles'][:5]):
            speak(f"{i+1}. {article['title']}")
    except:
        speak("Sorry, I couldn't fetch the news at this time.")

def send_email():
    """Send an email using SMTP"""
    speak("Who would you like to send an email to?")
    recipient = recognize_speech()
    if recipient:
        speak("What should the subject be?")
        subject = recognize_speech()
        if subject:
            speak("What message would you like to send?")
            message = recognize_speech()
            if message:
                try:
                    # Configure email settings
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    # You'll need to set up app password for this
                    server.login("your_email@gmail.com", "your_app_password")
                    email_message = f"Subject: {subject}\n\n{message}"
                    server.sendmail("your_email@gmail.com", recipient, email_message)
                    server.quit()
                    speak("Email sent successfully!")
                except:
                    speak("Sorry, I couldn't send the email.")

def control_music(command):
    """Control music playback using keyboard shortcuts"""
    if "play" in command or "pause" in command:
        pyautogui.press('playpause')
        speak("Playing or pausing music")
    elif "next" in command:
        pyautogui.press('nexttrack')
        speak("Playing next track")
    elif "previous" in command:
        pyautogui.press('prevtrack')
        speak("Playing previous track")
    elif "volume up" in command:
        pyautogui.press('volumeup', presses=5)
        speak("Increasing volume")
    elif "volume down" in command:
        pyautogui.press('volumedown', presses=5)
        speak("Decreasing volume")

calendar_data = {}

def manage_calendar():
    """Simple calendar management system"""
    speak("What would you like to do with your calendar?")
    command = recognize_speech()
    
    if "add" in command:
        speak("What event would you like to add?")
        event = recognize_speech()
        if event:
            speak("When is this event?")
            date = recognize_speech()
            if date:
                # Simple storage - in real app would use proper calendar API
                calendar_data[date] = event
                speak(f"Added {event} on {date}")
    elif "check" in command:
        speak("What date would you like to check?")
        date = recognize_speech()
        if date in calendar_data:
            speak(f"You have {calendar_data[date]} on {date}")
        else:
            speak(f"You have no events on {date}")

def get_system_info():
    """Get and report system information"""
    speak("Here's your system information:")
    system_info = f"Operating System: {platform.system()} {platform.version()}"
    processor = f"Processor: {platform.processor()}"
    memory = f"RAM: {round(psutil.virtual_memory().total / (1024.0 **3))} GB"
    
    speak(system_info)
    speak(processor)
    speak(memory)

def adjust_recognition_settings():
    """Adjust the speech recognition settings"""
    global recognizer
    
    speak("Adjusting speech recognition sensitivity.")
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Default is usually 300
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        speak("Please remain silent for a moment while I adjust for ambient noise.")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        speak("Noise adjustment complete.")

def ai_assistant():
    """Main AI assistant loop"""
    speak("Hello! Say 'may the force be with you' to activate me.")
    global recognizer
    recognizer = sr.Recognizer()
    
    while True:
        command = recognize_speech()
        if command is None:
            continue
        
        if "may the force be with you" in command:
            speak("Hello master, R2D2 reporting")
            
            while True:
                # Check for reminders every loop
                check_reminders()
                
                command = recognize_speech()
                if command is None:
                    continue
                
                # Original features
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
                elif "volume" in command and not ("up" in command or "down" in command):
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
                elif "remind" in command or "reminder" in command:
                    set_reminder()
                elif "news" in command or "headlines" in command:
                    get_news()
                elif "email" in command or "send mail" in command:
                    send_email()
                elif any(word in command for word in ["play music", "pause music", "next track", "previous track", "volume up", "volume down"]):
                    control_music(command)
                elif "calendar" in command:
                    manage_calendar()
                elif "system" in command or "computer info" in command:
                    get_system_info()
                elif "adjust" in command and "voice" in command:
                    adjust_recognition_settings()
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

if __name__ == "__main__":
    ai_assistant()
