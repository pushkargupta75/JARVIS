import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import google.generativeai as genai
import subprocess

# Configure Gemini API
GENAI_API_KEY = "AIzaSyD9lL6VDMGplLqoxRU1-REln3Gf20a3jpI"
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Set up text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.RequestError:
            print("Could not request results.")
            return None

def get_response_from_gemini(prompt):
    """Get a response from Gemini AI."""
    try:
        response = model.generate_content(prompt)
        return response.text if response else "Sorry, I couldn't understand."
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't process your request."

# Dictionary for opening applications
app_dict = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "command prompt": "cmd.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "chrome": "chrome.exe",
    "firefox": "firefox.exe",
    "paint": "mspaint.exe",
}

def open_app(command):
    for app in app_dict:
        if app in command:
            os.system(f"start {app_dict[app]}")
            speak(f"Opening {app}")
            return
    speak("Application not recognized or not in the list")

def perform_system_task(command):
    if "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 5")
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 5")
    elif "sleep" in command:
        speak("Putting the system to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "lock" in command:
        speak("Locking the system.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "task manager" in command:
        speak("Opening Task Manager.")
        os.system("taskmgr")
    elif "control panel" in command:
        speak("Opening Control Panel.")
        os.system("control")
    elif "file explorer" in command:
        speak("Opening File Explorer.")
        os.system("explorer")
    else:
        speak("Sorry, I can't perform that system task.")

def main():
    """Main function to run the voice assistant."""
    speak("Hello! I am Jarvis!! How can I assist you?")
    while True:
        user_input = listen()
        if user_input:
            # Stop command
            if "stop" in user_input or "jarvis stop" in user_input:
                speak("Alright, stopping now.")
                break

            # Exit command
            if "exit" in user_input or "over and out" in user_input:
                speak("Goodbye! Sir, have a nice day.")
                break

            # Handling website opening
            sites = {
                "youtube": "https://youtube.com",
                "wikipedia": "https://wikipedia.com",
                "google": "https://google.com",
                "chatgpt": "https://chat.openai.com"
            }
            for site, url in sites.items():
                if f"open {site}" in user_input:
                    webbrowser.open(url)
                    speak(f"Opening {site}")
                    break
            else:
                # Handling time request
                if "what is the time" in user_input:
                    st = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"The time is {st}")

                # Handling camera opening (Windows camera app)
                elif "open camera" in user_input:
                    os.system("start microsoft.windows.camera:")
                    speak("Opening camera")

                # Handling application opening
                elif any(app in user_input for app in app_dict):
                    open_app(user_input)

                # Handling system tasks
                elif any(task in user_input for task in
                         ["shutdown", "restart", "sleep", "lock", "task manager", "control panel", "file explorer"]):
                    perform_system_task(user_input)

                # Handling chatbot response
                else:
                    response = get_response_from_gemini(user_input)
                    print("Jarvis:", response)
                    speak(response)

if __name__ == "__main__":
    main()