from gtts import gTTS
import os
from pathlib import Path
import base64

class TTSHandler:
    """Handles Text-to-Speech conversion for multiple languages"""
    
    # Language codes mapping for gTTS
    TTS_LANG_MAP = {
        'en': 'en',
        'hi': 'hi',
        'bn': 'bn',
        'te': 'te',
        'mr': 'mr',
        'ta': 'ta',
        'gu': 'gu',
        'kn': 'kn',
        'ml': 'ml',
        'pa': 'pa',
    }
    
    def __init__(self):
        # Create audio directory if it doesn't exist
        self.audio_dir = Path("audio_files")
        self.audio_dir.mkdir(exist_ok=True)
    
    def text_to_speech(self, text, language='hi', filename=None):
        """
        Convert text to speech and save as MP3 file
        
        Args:
            text: Text to convert to speech
            language: Language code (e.g., 'hi', 'en')
            filename: Optional custom filename
            
        Returns:
            Path to the generated audio file or None if failed
        """
        try:
            # Get the correct language code for gTTS
            tts_lang = self.TTS_LANG_MAP.get(language, 'en')
            
            # Generate filename if not provided
            if filename is None:
                import hashlib
                text_hash = hashlib.md5(text.encode()).hexdigest()[:8]
                filename = f"response_{tts_lang}_{text_hash}.mp3"
            
            filepath = self.audio_dir / filename
            
            # Create TTS object
            tts = gTTS(text=text, lang=tts_lang, slow=False)
            
            # Save audio file
            tts.save(str(filepath))
            
            return filepath
            
        except Exception as e:
            print(f"TTS Error: {e}")
            return None
    
    def get_audio_base64(self, filepath):
        """
        Convert audio file to base64 for embedding in HTML
        
        Args:
            filepath: Path to audio file
            
        Returns:
            Base64 encoded string or None
        """
        try:
            with open(filepath, "rb") as audio_file:
                audio_bytes = audio_file.read()
                audio_base64 = base64.b64encode(audio_bytes).decode()
                return audio_base64
        except Exception as e:
            print(f"Base64 conversion error: {e}")
            return None
    
    def cleanup_old_files(self, max_files=50):
        """
        Clean up old audio files to save space
        Keep only the most recent files
        
        Args:
            max_files: Maximum number of files to keep
        """
        try:
            audio_files = sorted(
                self.audio_dir.glob("*.mp3"),
                key=os.path.getmtime,
                reverse=True
            )
            
            # Delete older files
            for old_file in audio_files[max_files:]:
                old_file.unlink()
                
        except Exception as e:
            print(f"Cleanup error: {e}")
    
    def delete_audio_file(self, filepath):
        """Delete a specific audio file"""
        try:
            if filepath and os.path.exists(filepath):
                os.remove(filepath)
        except Exception as e:
            print(f"Delete error: {e}")