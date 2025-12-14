"""
Helper functions for the chatbot
"""
import streamlit as st
import json
from pathlib import Path

def load_json_data(file_path):
    """Load JSON data from file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        st.error(f"Error loading JSON data: {str(e)}")
        return {}

def save_json_data(data, file_path):
    """Save data to JSON file"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"Error saving JSON data: {str(e)}")
        return False

def get_user_feedback():
    """Get user feedback on responses"""
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👍 उपयोगी"):
            st.success("धन्यवाद! आपकी प्रतिक्रिया हमारे लिए महत्वपूर्ण है।")
            return "positive"
    
    with col2:
        if st.button("👎 उपयोगी नहीं"):
            st.warning("हम बेहतर करने की कोशिश करेंगे।")
            return "negative"
    
    return None

def format_phone_number(number):
    """Format phone number for display"""
    if len(number) == 10:
        return f"{number[:3]}-{number[3:6]}-{number[6:]}"
    return number

def create_download_link(data, filename, text="Download"):
    """Create download link for data"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    st.download_button(
        label=text,
        data=json_str,
        file_name=filename,
        mime="application/json"
    )

def log_interaction(user_query, bot_response, language):
    """Log user interactions for analytics"""
    try:
        log_entry = {
            "timestamp": str(st.session_state.get('current_time')),
            "user_query": user_query,
            "bot_response": bot_response,
            "language": language,
            "session_id": st.session_state.get('session_id', 'unknown')
        }
        
        # In a real application, you would save this to a database
        # For now, we'll just store in session state
        if 'interaction_logs' not in st.session_state:
            st.session_state.interaction_logs = []
        
        st.session_state.interaction_logs.append(log_entry)
        
    except Exception as e:
        # Don't show error to user for logging issues
        pass

def validate_input(text, max_length=500):
    """Validate user input"""
    if not text or not text.strip():
        return False, "कृपया अपना प्रश्न लिखें।"
    
    if len(text) > max_length:
        return False, f"प्रश्न {max_length} अक्षरों से कम होना चाहिए।"
    
    return True, "Valid"

def get_session_stats():
    """Get session statistics"""
    stats = {
        'messages_count': len(st.session_state.get('messages', [])),
        'language': st.session_state.get('selected_language', 'hi'),
        'interactions': len(st.session_state.get('interaction_logs', []))
    }
    return stats