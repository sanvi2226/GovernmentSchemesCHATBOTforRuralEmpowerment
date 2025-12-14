import speech_recognition as sr
from deep_translator import GoogleTranslator
from langdetect import detect

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def record_and_recognize(self, target_lang="hi"):
        """Listen to user's voice and convert it to Hindi text"""
        with self.microphone as source:
            print("🎙️ Speak now...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)

        try:
            print("🧠 Recognizing speech...")
            # Recognize speech in default language (Google automatically detects)
            text = self.recognizer.recognize_google(audio)
            print(f"User said: {text}")

            # Detect spoken language
            detected_lang = detect(text)
            print(f"Detected language: {detected_lang}")

            # If the spoken language isn't Hindi, translate it to Hindi for consistency
            if detected_lang != target_lang:
                translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
                print(f"Translated to Hindi: {translated_text}")
                return translated_text
            else:
                return text

        except sr.UnknownValueError:
            return "माफ करें, मैं आपकी आवाज़ नहीं समझ पाया। कृपया दोबारा बोलें।"
        except sr.RequestError:
            return "नेटवर्क त्रुटि: कृपया अपना इंटरनेट कनेक्शन जांचें।"
