# Jarvis Voice Assistant

Jarvis is a Python-based voice assistant that can recognize and respond to voice commands. It performs a variety of tasks such as opening websites, managing files, providing weather updates, retrieving information from Wikipedia, and setting reminders. It uses Python libraries for speech recognition, text-to-speech, web scraping, and more.

## Features

- **Voice Recognition**: The assistant responds to voice commands using the `SpeechRecognition` library.
- **Text-to-Speech**: Converts Jarvis' responses to spoken words using the `pyttsx3` library.
- **Web Automation**: Jarvis can open popular websites such as Google, Facebook, YouTube, Instagram, and LinkedIn using the `webbrowser` module.
- **Weather Updates**: Provides real-time weather updates by scraping data from websites.
- **Wikipedia Integration**: Fetches brief summaries of topics from Wikipedia.
- **Task Automation**: Opens Notepad and allows setting text-based reminders.
- **File Management**: Opens files present on the system by voice command.

## Technologies Used

- **Python**: The core programming language used.
- **SpeechRecognition**: For recognizing user voice commands.
- **Pyttsx3**: For converting text to speech.
- **Webbrowser**: For opening websites via voice commands.
- **BeautifulSoup**: For scraping weather data from web pages.
- **Wikipedia API**: For retrieving information from Wikipedia.
- **Subprocess**: For automating tasks like opening Notepad.
- **Requests**: For making HTTP requests to fetch data from websites.

## How It Works

1. **Initialization**: Jarvis listens for the wake word "Jarvis." Once activated, it waits for the user to give a command.
2. **Processing Commands**: Based on the command, Jarvis performs one of the following tasks:
   - Opens a popular website like Google, Facebook, or LinkedIn.
   - Provides the current weather for a specified city using web scraping.
   - Retrieves a brief summary from Wikipedia.
   - Automates tasks like opening Notepad or setting reminders.
   - Opens a specified file if it exists on the system.

## Setup Instructions

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed using `pip`):
  ```bash
  pip install speechrecognition pyttsx3 wikipedia requests beautifulsoup4
