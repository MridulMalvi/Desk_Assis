# Gemassist 🎙️

> A Python-based, voice-activated desktop assistant powered by Google Gemini 2.5 Flash.

Gemassist listens to your voice, understands your intent, and responds — all hands-free. It combines Google's Gemini AI for intelligent conversation with Python's speech recognition and text-to-speech libraries on Windows.

---

## Features

- 🧠 **Conversational AI** — Gemini 2.5 Flash handles complex, open-ended queries
- 👂 **Voice Recognition** — Captures and transcribes microphone audio via `speech_recognition`
- 🔊 **Text-to-Speech** — Speaks responses aloud using `pyttsx3`
- 🕐 **Date & Time** — Fetches and announces the current local time and date
- 🔍 **Web Search** — Voice-triggered Google and YouTube searches
- 🖥️ **App Launcher** — Opens Windows apps and websites by voice

---

## Installation

**Requirements:** Python 3.7+, Windows, working microphone, [Gemini API key](https://aistudio.google.com/app/apikey)

```bash
pip install SpeechRecognition pyttsx3 google-genai PyAudio
```

> If `PyAudio` fails on Windows, download the pre-built wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.

---

## Configuration

Set your Gemini API key as an environment variable (recommended over hardcoding):

```bash
set GEMINI_API_KEY=your_api_key_here   # Windows CMD
```

Then update `assistant.py`:

```python
import os
api_key = os.environ.get("GEMINI_API_KEY")
```

> ⚠️ Never commit your API key to version control.

---

## Usage

```bash
python assistant.py
```

The assistant greets you with *"Hey I am online. How can I help you?"* and starts listening. Say **"Stop"** or **"Exit"** to quit.

---

## Voice Commands

| Category | Example Commands |
|---|---|
| **Time & Date** | `"What time is it?"`, `"Today's date"` |
| **Google Search** | `"Search Google for [query]"` |
| **YouTube Search** | `"Search YouTube for [query]"` |
| **Websites** | `"Open Google"`, `"Open YouTube"`, `"Open Instagram"` |
| **MS Office** | `"Open Word"`, `"Open Excel"`, `"Open PowerPoint"` |
| **Apps** | `"Open VS Code"`, `"Open Notepad"`, `"Open Calculator"`, `"Open CMD"`, `"Open Camera"` |
| **AI Query** | Anything else → sent to Gemini AI |
| **Exit** | `"Stop"`, `"Exit"` |

---

## Project Structure

```
gemassist/
├── assistant.py   # Core logic — listening loop, command parser, Gemini API, app launchers
├── main.py        # Legacy script using win32com.client for basic TTS
└── README.md
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `google-genai` | Gemini 2.5 Flash API client |
| `SpeechRecognition` | Microphone audio capture & transcription |
| `pyttsx3` | Offline text-to-speech |
| `PyAudio` | Audio I/O backend for SpeechRecognition |

---

*Built with Python · Powered by Google Gemini 2.5 Flash*
