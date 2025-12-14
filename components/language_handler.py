from deep_translator import GoogleTranslator
from langdetect import detect, LangDetectException
import speech_recognition as sr

class LanguageHandler:
    """Handles translation between different languages"""
    
    # Supported languages with their codes and native names
    LANGUAGES = {
        'en': 'English',
        'hi': 'हिन्दी (Hindi)',
        'bn': 'বাংলা (Bengali)',
        'te': 'తెలుగు (Telugu)',
        'mr': 'मराठी (Marathi)',
        'ta': 'தமிழ் (Tamil)',
        'gu': 'ગુજરાતી (Gujarati)',
        'kn': 'ಕನ್ನಡ (Kannada)',
        'ml': 'മലയാളം (Malayalam)',
        'pa': 'ਪੰਜਾਬੀ (Punjabi)',
        'or': 'ଓଡ଼ିଆ (Odia)',
        'as': 'অসমীয়া (Assamese)'
    }
    
    # Language code mapping for speech recognition
    SPEECH_LANG_MAP = {
        'en': 'en-IN',
        'hi': 'hi-IN',
        'bn': 'bn-IN',
        'te': 'te-IN',
        'mr': 'mr-IN',
        'ta': 'ta-IN',
        'gu': 'gu-IN',
        'kn': 'kn-IN',
        'ml': 'ml-IN',
        'pa': 'pa-IN',
        'or': 'or-IN',
        'as': 'as-IN'
    }
    
    def __init__(self):
        self.translator = GoogleTranslator()
        self.recognizer = sr.Recognizer()
    
    def translate_text(self, text, source_lang='auto', target_lang='en'):
        """
        Translate text from source language to target language
        
        Args:
            text: Text to translate
            source_lang: Source language code (default: 'auto' for auto-detection)
            target_lang: Target language code
            
        Returns:
            Translated text or original text if translation fails
        """
        try:
            if source_lang == target_lang:
                return text
            
            translated = GoogleTranslator(
                source=source_lang, 
                target=target_lang
            ).translate(text)
            
            return translated
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def detect_language(self, text):
        """
        Detect the language of given text
        
        Args:
            text: Text to detect language for
            
        Returns:
            Language code or 'en' if detection fails
        """
        try:
            detected = detect(text)
            return detected
        except LangDetectException:
            return 'en'
    
    def recognize_speech(self, audio_data, language='hi'):
        """
        Recognize speech from audio data in specified language
        
        Args:
            audio_data: Audio data from microphone
            language: Language code for recognition
            
        Returns:
            Recognized text or error message
        """
        try:
            # Get the proper language code for speech recognition
            speech_lang = self.SPEECH_LANG_MAP.get(language, 'en-IN')
            
            # Recognize speech
            text = self.recognizer.recognize_google(audio_data, language=speech_lang)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
    
    @staticmethod
    def get_language_options():
        """Returns list of tuples for language selection dropdown"""
        return [(code, name) for code, name in LanguageHandler.LANGUAGES.items()]