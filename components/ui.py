import streamlit as st


def render_header():
    st.markdown("<h1 style='text-align:center; color:green;'>🏛️ Empower Chatbot - Government Schemes Assist</h1>", unsafe_allow_html=True)
    st.markdown("---")

def render_sidebar():
    st.sidebar.subheader("About")
    st.sidebar.write("This chatbot helps rural citizens understand government schemes easily.")

def render_chat_interface(chatbot):
    """Render the main chat interface"""
    # Chat messages container
    chat_container = st.container()
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    
    with chat_container:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Input section
    st.markdown("---")
    
        
    prompt = st.chat_input()
        
    if prompt:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
            
        with st.spinner("Analyzing documents and preparing a simple answer..."):
            response = st.session_state.chatbot.generate_answer(prompt) 
           

        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
            
        st.rerun()
    
