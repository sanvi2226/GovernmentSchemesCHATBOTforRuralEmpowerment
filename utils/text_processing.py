"""
Text processing utilities
"""
import re
import string

def clean_text(text):
    """Clean and preprocess text"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep Hindi characters
    text = re.sub(r'[^\w\s\u0900-\u097F]', ' ', text)
    
    # Strip and return
    return text.strip()

def extract_keywords(text, language='hi'):
    """Extract keywords from text"""
    if not text:
        return []
    
    # Common stop words in Hindi and English
    stop_words_hi = {'और', 'का', 'की', 'के', 'में', 'से', 'को', 'है', 'हैं', 'था', 'थे', 'होगा', 'होंगे'}
    stop_words_en = {'the', 'is', 'at', 'which', 'on', 'and', 'or', 'but', 'in', 'with'}
    
    stop_words = stop_words_hi if language == 'hi' else stop_words_en
    
    # Split text and filter stop words
    words = text.lower().split()
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    return keywords

def format_scheme_info(scheme):
    """Format scheme information for display"""
    formatted = f"""
    **{scheme['scheme']}**
    
    📝 **विवरण:** {scheme['description']}
    
    ✅ **पात्रता:** {scheme['eligibility']}
    
    💰 **लाभ:** {scheme['benefits']}
    
    📋 **आवेदन प्रक्रिया:** {scheme['application']}
    """
    
    return formatted.strip()

def detect_intent(text):
    """Detect user intent from text"""
    text_lower = text.lower()
    
    # Define intent patterns
    intents = {
        'scheme_inquiry': ['योजना', 'scheme', 'policy', 'नीति', 'सहायता', 'help'],
        'application_help': ['आवेदन', 'apply', 'application', 'form', 'फॉर्म'],
        'eligibility': ['पात्रता', 'eligible', 'qualification', 'योग्यता'],
        'benefits': ['लाभ', 'benefit', 'फायदा', 'advantage'],
        'documents': ['दस्तावेज', 'document', 'papers', 'कागज']
    }
    
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in text_lower:
                return intent
    
    return 'general_inquiry'