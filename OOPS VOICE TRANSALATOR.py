import pyaudio
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

class VoiceTranslator:
    def __init__(self, src_lang='en', dest_lang='hi'):
        self.src_lang = src_lang
        self.dest_lang = dest_lang
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.translated_audio_file = 'translated_audio.mp3'

    def record_audio(self, duration=5):
        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 1
        fs = 44100
        p = pyaudio.PyAudio()

        print("Recording...")
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []
        for _ in range(0, int(fs / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        audio_data = b''.join(frames)
        return audio_data, p.get_sample_size(sample_format)

    def recognize_speech(self, audio_data, sample_width):
        audio = sr.AudioData(audio_data, 44100, sample_width)
        try:
            text = self.recognizer.recognize_google(audio, language=self.src_lang)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    def translate_text(self, text):
        translation = self.translator.translate(text, src=self.src_lang, dest=self.dest_lang)
        print(f"Translated Text: {translation.text}")
        return translation.text

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang=self.dest_lang)
        tts.save(self.translated_audio_file)
        playsound.playsound(self.translated_audio_file)
        os.remove(self.translated_audio_file)

    def translate_voice(self):
        audio_data, sample_width = self.record_audio()
        text = self.recognize_speech(audio_data, sample_width)
        if text:
            translated_text = self.translate_text(text)
            self.text_to_speech(translated_text)

if __name__ == "__main__":
    vt = VoiceTranslator(src_lang='en', dest_lang='hi')
    vt.translate_voice()
