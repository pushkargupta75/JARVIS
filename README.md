# Jarvis - AI Voice Assistant

Jarvis is a Python-based AI voice assistant that performs basic system tasks and provides intelligent responses using the Gemini API. It allows users to interact with their system using voice commands and automates tasks such as opening applications, fetching information, and browsing the web.

## Features
- **Speech Recognition**: Listens to voice commands using the `speech_recognition` module.
- **Text-to-Speech (TTS)**: Responds using a TTS engine for a natural conversational experience.
- **Application Control**: Opens applications like Notepad, Chrome, and File Explorer.
- **Web Automation**: Opens websites based on user requests.
- **System Tasks**: Fetches the current time, opens the camera, and performs system operations.
- **AI-Powered Responses**: Answers queries using the Gemini API.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  ```bash
  pip install speechrecognition pyttsx3 requests
  ```
- API key for Gemini (Google AI API) for intelligent responses.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd jarvis-voice-assistant
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Gemini API key:
   ```python
   API_KEY = "your_gemini_api_key_here"
   ```

## Usage
Run the script to activate Jarvis:
```bash
python main4.py
```
Then, speak into the microphone and Jarvis will execute your commands.

## Example Commands
- "Open Chrome"
- "What is the current time?"
- "Open YouTube"
- "Tell me a joke"
- "Who is Albert Einstein?"

## Contributing
Feel free to fork this repository and contribute by submitting pull requests. Suggestions and improvements are always welcome!

## License
This project is licensed under the MIT License.

## Author
Pushkar Gupta
pushkargupta993@gmail.com

---

Enjoy using Jarvis, your personal AI assistant! 🚀

