# R2D2 AI Voice Assistant

A powerful voice-activated assistant that responds to commands and performs various tasks through speech recognition and text-to-speech capabilities.

## Features

### Core Functionality
- **Voice Recognition**: Listens for commands using Google's speech recognition API
- **Text-to-Speech**: Responds verbally using pyttsx3
- **Wake Phrase**: Activated by saying "may the force be with you"

### System Controls
- Check time and date
- Open applications (notepad, calculator, Chrome, Spotify, etc.)
- Control system volume
- Adjust screen brightness

### Information Services
- Weather updates for any city
- Wikipedia searches with summarized results
- Web searches through Google

### Entertainment
- Random jokes from pyjokes
- Small talk conversations
- AI-powered responses using g4f

### Task Management
- **Reminders**: Set and receive time-based reminders
- **Calendar**: Add and check events on specific dates

### Communication
- **Email**: Send emails through voice commands
- **News Reader**: Get the latest headlines from News API

### Media Controls
- Play/pause music
- Skip to next/previous track
- Adjust volume up/down

### System Tools
- **System Information**: Get details about OS, processor, and RAM
- **Voice Recognition Settings**: Adjust for ambient noise and sensitivity

## Requirements

### Python Packages
```
speech_recognition
pyttsx3
webbrowser
requests
wikipedia
g4f
pyjokes
smtplib
screen_brightness_control
pycaw
psutil
pyautogui
```

### APIs
- Weather API key
- News API key
- Gmail credentials (for email functionality)

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/r2d2-assistant.git
cd r2d2-assistant
```

2. Install required packages:
```
pip install -r requirements.txt
```

3. Configure API keys:
   - Replace `"YOUR_API_KEY"` in the weather function
   - Replace `"YOUR_NEWS_API_KEY"` in the news function
   - Configure email credentials in the send_email function

## Usage

1. Run the assistant:
```
python r2d2_assistant.py
```

2. Say the wake phrase: "may the force be with you"

3. After hearing "Hello master, R2D2 reporting", issue commands like:
   - "What's the weather in London?"
   - "Tell me a joke"
   - "Open Chrome"
   - "Set a reminder"
   - "Send an email"
   - "Play music"
   - "Check my calendar"
   - "Get system information"

4. To exit, say "goodbye" or "exit"

## Command Examples

| Feature | Example Command |
|---------|----------------|
| Weather | "What's the weather in Tokyo?" |
| Time/Date | "What time is it?" or "What's today's date?" |
| Applications | "Open calculator" |
| Jokes | "Tell me a joke" |
| Web Search | "Search for how to make pasta" |
| Reminders | "Set a reminder" |
| News | "Read the news headlines" |
| Email | "Send an email" |
| Music | "Play music" or "Next track" |
| Calendar | "Check my calendar" or "Add to calendar" |
| System Info | "Get system information" |
| Voice Settings | "Adjust voice recognition" |

## Customization

- Add new applications to the `apps` dictionary in the `open_application` function
- Expand small talk responses in the `small_talk` function
- Modify the assistant's name or wake phrase in the code

## Future Enhancements

Potential features to add:
- Text message sending via Twilio
- Home automation integration
- Meeting scheduler/joiner
- Screen recorder
- File management
- To-do list management
- Voice authentication
- Natural language timers
- Currency converter
- Podcast/audiobook player
- Fitness tracking integration
- Recipe assistant
- Travel information
- Voice notes
- Language learning helper

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
