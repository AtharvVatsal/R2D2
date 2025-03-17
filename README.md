# AI Voice Assistant

A voice-controlled AI assistant built using Python that can perform various tasks such as speech recognition, text-to-speech conversion, web searches, weather updates, application launching, and more.

## Features

- **Speech Recognition**: Uses Google Speech Recognition to process voice commands.
- **Text-to-Speech**: Converts text responses to speech using `pyttsx3`.
- **Weather Updates**: Fetches real-time weather data.
- **Wikipedia Search**: Retrieves brief summaries from Wikipedia.
- **Web Search**: Opens Google search results for a given query.
- **Jokes**: Generates random jokes.
- **Application Launcher**: Opens commonly used applications.
- **Volume & Brightness Control**: Adjusts system volume and screen brightness.
- **AI Response**: Uses GPT-based responses for queries.

## Requirements

Ensure you have the following Python libraries installed:

```sh
pip install speechrecognition pyttsx3 requests wikipedia pyjokes screen-brightness-control pycaw g4f
```

## Usage

1. Run the script:
   ```sh
   python assistant.py
   ```
2. Say "May the force be with you" to activate the assistant.
3. Give voice commands like:
   - "What's the weather in New Delhi?"
   - "Tell me a joke."
   - "Open Notepad."
   - "Search Wikipedia for Albert Einstein."
   - "Increase volume to 70%."
   - "Set brightness to 50%."
4. Say "Goodbye" to exit.

## Configuration

- Modify the `apps` dictionary to add new applications.
- Update `API_KEY` in `get_weather()` with your OpenWeather API key.

## Future Enhancements

- Add email automation.
- Integrate with smart home devices.
- Improve AI response handling.

## License

This project is open-source and available for modification.

---

Enjoy your AI assistant! 🚀


