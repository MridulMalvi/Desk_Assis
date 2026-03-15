import os
import speech_recognition as sr
import pyttsx3
from google import genai
import re
import webbrowser
import datetime

# CONFIGURATION 
os.environ["GEMINI_API_KEY"] = "AIzaSyD2aU_Gtg4dMWQZdKDp3Gea4TKzIY_kC3M"

# 1. The "Brain" (Gemini API)
client = genai.Client()

def ask_gemini(question):
    print("Thinking...")
    prompt = question + " (Reply in 1 or 2 short sentences. Do not use asterisks, bolding, emojis, or any markdown. Use plain text only.)"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    clean_text = re.sub(r'[^a-zA-Z0-9.,!?\' ]', '', response.text) 
    return clean_text

# 2. The "Ears" (Speech-to-Text)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except:
        return ""

# 3. The "Mouth" (Text-to-Speech)
def speak(text):
    print(f"\nAI: {text}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 170) 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# 4. The Main Loop
def main():
    speak("Hey I am online. How can I help you?")
    
    while True:
        command = listen()
        
        if command == "":
            continue
            
        # --- TIME & DATE ACTIONS ---
        if "what time is it" in command or "current time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")
            
        elif "what is the date" in command or "today's date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today is {current_date}")

        # --- DYNAMIC SEARCHES ---
        elif "search google for" in command:
            query = command.replace("search google for", "").strip()
            speak(f"Searching Google for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif "search youtube for" in command:
            query = command.replace("search youtube for", "").strip()
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            
        # --- WEB ACTIONS ---
        elif "open chrome" in command or "open google" in command:
            speak("Opening Google Chrome")
            webbrowser.open("https://www.google.com")

        elif "open instagram" in command:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")
            
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            
        # --- NEW: OFFICE & CAMERA ACTIONS ---
        elif "open word" in command or "open ms word" in command:
            speak("Opening Microsoft Word")
            os.system("start winword")

        elif "open excel" in command or "open ms excel" in command:
            speak("Opening Microsoft Excel")
            os.system("start excel")

        elif "open powerpoint" in command or "open ppt" in command:
            speak("Opening Microsoft PowerPoint")
            os.system("start powerpnt")

        elif "open camera" in command:
            speak("Opening Camera")
            # Uses the Windows 10/11 URI to launch the built-in Camera app
            os.system("start microsoft.windows.camera:")

        # --- DEV TOOLS ---
        elif "open vs code" in command or "open visual studio" in command:
            speak("Opening VS Code")
            os.system("code")
            
        elif "open command prompt" in command or "open cmd" in command:
            speak("Opening Command Prompt")
            os.system("start cmd")

        # --- BASIC DESKTOP ACTIONS ---
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")
            
        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")
            
        elif "stop" in command or "exit" in command:
            speak("Shutting down.")
            break
            
        # --- AI CHAT ---
        else:
            answer = ask_gemini(command)
            speak(answer)

if __name__ == "__main__":
    main()