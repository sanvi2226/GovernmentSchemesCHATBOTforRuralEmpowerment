import streamlit as st
from components.chatbot import GovernmentChatbot
from components.language_handler import LanguageHandler
from components.ui_components import render_header, render_sidebar
from components.ui_components import render_chat_interface
from components.ui_components import render_welcome_message
from components.tts_handler import TTSHandler  # NEW

st.set_page_config(page_title="Empower Chatbot", page_icon="🏛️", layout="wide")


def main():
    st.sidebar.header("Rural Chatbot")

    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = GovernmentChatbot()
    # Initialize language handler
    if 'language_handler' not in st.session_state:
        st.session_state.language_handler = LanguageHandler()
    # Initialize TTS handler
    if 'tts_handler' not in st.session_state:
        st.session_state.tts_handler = TTSHandler()

    # Initialize selected language (default to Hindi)
    if 'selected_language' not in st.session_state:
        st.session_state.selected_language = 'en'

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if st.sidebar.button("🔄 Refresh Knowledge Base"):
        import subprocess
        with st.spinner("Updating FAISS index..."):
            result = subprocess.run(["python", "scripts/embed_pdfs.py"], capture_output=True, text=True)
            st.success("✅ Knowledge base updated successfully!")
            st.text(result.stdout)

    # UI
    render_header()
    render_sidebar()

    render_welcome_message()
    # Main chat interface
    render_chat_interface(st.session_state.chatbot)


if __name__ == "__main__":
    main()
