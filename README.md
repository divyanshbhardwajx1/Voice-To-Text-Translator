# Voice-To-Text-Translator

A real-time voice translator that captures spoken language, converts it to text, translates it into a desired language, and then plays the translated speech using text-to-speech technology.

## 🚀 Features

- Real-time voice input using a microphone.
- Translation between multiple languages using Google Translate API.
- Text-to-speech output in the translated language.
- MP3 file generation and playback.
- Temporary audio files automatically deleted after use.

## 🛠️ Technologies & Libraries Used

- **Python 3**
- `speech_recognition` – For converting speech to text.
- `pyaudio` – To capture audio input from the user.
- `googletrans` – To translate the recognized text.
- `gtts` – Google Text-to-Speech for audio generation.
- `playsound` – For playing the translated speech.
- `os` – To handle file operations (like deletion).

---

## 📦 Installation

Make sure Python 3.x is installed. Then, install the required libraries using:

```bash
pip install SpeechRecognition pyaudio googletrans==4.0.0-rc1 gtts playsound
