import streamlit as st

def inject_custom_css():
    """Inject custom CSS for rural-friendly, accessible UI"""
    st.markdown("""
    <style>
    /* ============================================
       GLOBAL STYLES & RESET
       ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans', 'Segoe UI', Arial, sans-serif;
    }
    
    /* Main app background with subtle gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7f0 0%, #e8f5e9 50%, #fff8e1 100%);
        background-attachment: fixed;
    }
    
    /* ============================================
       COLOR PALETTE
       ============================================ */
    :root {
        --primary-green: #2e7d32;
        --light-green: #66bb6a;
        --accent-green: #81c784;
        --soil-brown: #8d6e63;
        --light-brown: #a1887f;
        --sky-blue: #4fc3f7;
        --light-yellow: #fff9c4;
        --cream: #fffde7;
        --white: #ffffff;
        --text-dark: #2c3e21;
        --text-medium: #4a5d3f;
        --shadow: rgba(0, 0, 0, 0.1);
        --shadow-strong: rgba(0, 0, 0, 0.15);
    }
    
    /* ============================================
       HEADER STYLING
       ============================================ */
    h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: var(--primary-green) !important;
        text-align: center !important;
        padding: 1.5rem 1rem !important;
        margin-bottom: 0 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        line-height: 1.4 !important;
    }
    
    /* Decorative header banner */
    .header-banner {
        background: linear-gradient(135deg, #2e7d32 0%, #66bb6a 50%, #81c784 100%);
        padding: 2rem 1rem;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 4px 20px var(--shadow-strong);
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .header-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 300px;
        height: 300px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
    }
    
    .header-banner::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -5%;
        width: 200px;
        height: 200px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 50%;
    }
    
    /* ============================================
       SIDEBAR STYLING
       ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f5f7f0 100%);
        border-right: 3px solid var(--accent-green);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] h3 {
        color: var(--primary-green);
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--accent-green);
    }
    
    [data-testid="stSidebar"] p {
        color: var(--text-medium);
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* ============================================
       CHAT CONTAINER
       ============================================ */
    .main-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Chat message container */
    [data-testid="stChatMessageContainer"] {
        padding: 1.5rem 0;
    }
    
    /* ============================================
       CHAT BUBBLES - USER MESSAGES
       ============================================ */
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: linear-gradient(135deg, #4fc3f7 0%, #29b6f6 100%);
        border-radius: 20px 20px 5px 20px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0 1rem auto;
        max-width: 75%;
        box-shadow: 0 3px 12px rgba(79, 195, 247, 0.3);
        animation: slideInRight 0.4s ease-out;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }
    
    [data-testid="stChatMessage"][data-testid*="user"] p {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        margin: 0 !important;
        font-weight: 500 !important;
    }
    
    /* ============================================
       CHAT BUBBLES - ASSISTANT MESSAGES
       ============================================ */
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
        border-radius: 20px 20px 20px 5px;
        padding: 1.2rem 1.5rem;
        margin: 1rem auto 1rem 0;
        max-width: 80%;
        box-shadow: 0 3px 12px var(--shadow);
        border-left: 4px solid var(--primary-green);
        animation: slideInLeft 0.4s ease-out;
    }
    
    [data-testid="stChatMessage"][data-testid*="assistant"] p {
        color: var(--text-dark) !important;
        font-size: 1.1rem !important;
        line-height: 1.8 !important;
        margin: 0.5rem 0 !important;
    }
    
    [data-testid="stChatMessage"][data-testid*="assistant"] strong {
        color: var(--primary-green);
        font-weight: 600;
    }
    
    [data-testid="stChatMessage"][data-testid*="assistant"] ul,
    [data-testid="stChatMessage"][data-testid*="assistant"] ol {
        margin: 1rem 0 !important;
        padding-left: 1.5rem !important;
    }
    
    [data-testid="stChatMessage"][data-testid*="assistant"] li {
        margin: 0.5rem 0 !important;
        line-height: 1.7 !important;
    }
    
    /* ============================================
       CHAT INPUT BOX
       ============================================ */
    [data-testid="stChatInput"] {
        background: white;
        border-radius: 25px;
        padding: 0.5rem;
        box-shadow: 0 4px 20px var(--shadow-strong);
        border: 2px solid var(--accent-green);
        margin-top: 1.5rem;
    }
    
    [data-testid="stChatInput"] textarea {
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        padding: 1rem 1.5rem !important;
        border: none !important;
        color: var(--text-dark) !important;
        min-height: 60px !important;
    }
    
    [data-testid="stChatInput"] textarea::placeholder {
        color: var(--text-medium) !important;
        opacity: 0.6;
        font-size: 1.05rem !important;
    }
    
    [data-testid="stChatInput"] textarea:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Send button styling */
    [data-testid="stChatInput"] button {
        background: linear-gradient(135deg, var(--primary-green), var(--light-green)) !important;
        color: white !important;
        border-radius: 50% !important;
        padding: 0.8rem !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(46, 125, 50, 0.3) !important;
    }
    
    [data-testid="stChatInput"] button:hover {
        transform: scale(1.1) rotate(15deg) !important;
        box-shadow: 0 4px 16px rgba(46, 125, 50, 0.5) !important;
    }
    
    /* ============================================
       ANIMATIONS
       ============================================ */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* ============================================
       SPINNER & LOADING STATES
       ============================================ */
    [data-testid="stSpinner"] > div {
        border-top-color: var(--primary-green) !important;
        border-right-color: var(--light-green) !important;
    }
    
    .stSpinner > div {
        text-align: center;
        color: var(--primary-green);
    }
    
    /* ============================================
       DIVIDER
       ============================================ */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            var(--accent-green) 50%, 
            transparent 100%);
        margin: 2rem 0;
        opacity: 0.3;
    }
    
    /* ============================================
       BUTTONS & INTERACTIVE ELEMENTS
       ============================================ */
    .stButton button {
        background: linear-gradient(135deg, var(--primary-green), var(--light-green));
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.3);
        cursor: pointer;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(46, 125, 50, 0.4);
    }
    
    .stButton button:active {
        transform: translateY(0);
    }
    
    /* ============================================
       MOBILE RESPONSIVE (max-width: 768px)
       ============================================ */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.6rem !important;
            padding: 1rem 0.5rem !important;
        }
        
        .header-banner {
            padding: 1.5rem 0.5rem;
            border-radius: 0 0 20px 20px;
            margin-bottom: 1rem;
        }
        
        [data-testid="stChatMessage"][data-testid*="user"],
        [data-testid="stChatMessage"][data-testid*="assistant"] {
            max-width: 90%;
            padding: 1rem 1.2rem;
            font-size: 1.05rem;
        }
        
        [data-testid="stChatMessage"] p {
            font-size: 1.05rem !important;
        }
        
        [data-testid="stChatInput"] textarea {
            font-size: 1rem !important;
            padding: 0.8rem 1rem !important;
        }
        
        .main-container {
            padding: 0.5rem;
        }
        
        [data-testid="stSidebar"] {
            padding: 1rem 0.5rem;
        }
    }
    
    /* ============================================
       ACCESSIBILITY ENHANCEMENTS
       ============================================ */
    /* High contrast focus indicators */
    *:focus-visible {
        outline: 3px solid var(--primary-green) !important;
        outline-offset: 2px !important;
    }
    
    /* Ensure minimum touch target size */
    button, 
    [role="button"],
    a {
        min-height: 44px;
        min-width: 44px;
    }
    
    /* Better link visibility */
    a {
        color: var(--primary-green);
        text-decoration: underline;
        font-weight: 600;
    }
    
    a:hover {
        color: var(--light-green);
    }
    
    /* Screen reader only class */
    .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border-width: 0;
    }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render enhanced header with decorative banner"""
    inject_custom_css()
    
    st.markdown("""
    <div class="header-banner">
        <h1>🌾 सरकारी योजना सहायक | Government Schemes Assistant</h1>
        <p style='text-align:center; color: white; font-size: 1.1rem; margin-top: 0.5rem; font-weight: 500;'>
            आपकी सेवा में, आसान भाषा में | Serving you in simple language
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    """Render enhanced sidebar with scheme categories"""
    st.sidebar.markdown("### 📚 About This Assistant")
    st.sidebar.write("""
    This chatbot helps rural citizens understand government schemes easily. 
    Ask questions in simple language about:
    
    🌾 **Agriculture Schemes**
    - PM-KISAN, crop insurance
    
    🏥 **Health & Welfare**
    - Ayushman Bharat, insurance
    
    🏠 **Housing & Infrastructure**
    - PM Awas Yojana, rural housing
    
    💼 **Employment & Skills**
    - MGNREGA, skill development
    
    👨‍👩‍👧 **Social Welfare**
    - Pension schemes, women empowerment
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style='background: linear-gradient(135deg, #e8f5e9, #fff9c4); 
                padding: 1rem; 
                border-radius: 15px; 
                border-left: 4px solid #2e7d32;'>
        <p style='color: #2c3e21; font-weight: 600; margin: 0;'>
            💡 Tip: Ask in Hindi or English!
        </p>
        <p style='color: #4a5d3f; font-size: 0.95rem; margin: 0.5rem 0 0 0;'>
            Type your question naturally and get clear answers.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_chat_interface(chatbot):
    """Render the main chat interface with enhanced styling"""
    # Chat messages container
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Input section with enhanced prompt
    prompt = st.chat_input("💬 अपना सवाल यहाँ लिखें | Type your question here...")
        
    if prompt:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
            
        with st.spinner("🔍 Analyzing documents and preparing a simple answer..."):
            response = st.session_state.chatbot.generate_answer(prompt)

        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})
            
        st.rerun()


def render_welcome_message():
    """Display welcome message when chat is empty"""
    if len(st.session_state.messages) == 0:
        st.markdown("""
        <div style='text-align: center; padding: 3rem 1rem; animation: fadeIn 1s ease-in;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🙏</div>
            <h2 style='color: #2e7d32; font-weight: 600; margin-bottom: 1rem;'>
                Welcome! आपका स्वागत है!
            </h2>
            <p style='color: #4a5d3f; font-size: 1.2rem; line-height: 1.8; max-width: 600px; margin: 0 auto;'>
                Ask me anything about government schemes for rural citizens.<br>
                मुझसे सरकारी योजनाओं के बारे में कुछ भी पूछें।
            </p>
            <div style='margin-top: 2rem; padding: 1.5rem; 
                        background: linear-gradient(135deg, #f1f8f4, #fffde7); 
                        border-radius: 20px; 
                        max-width: 500px; 
                        margin-left: auto; 
                        margin-right: auto;
                        border: 2px solid #81c784;'>
                <p style='color: #2c3e21; font-weight: 600; margin-bottom: 0.5rem;'>
                    Example Questions:
                </p>
                <p style='color: #4a5d3f; margin: 0.3rem 0;'>
                    • "PM-KISAN scheme ke liye kaise apply karein?"
                </p>
                <p style='color: #4a5d3f; margin: 0.3rem 0;'>
                    • "What is Ayushman Bharat scheme?"
                </p>
                <p style='color: #4a5d3f; margin: 0.3rem 0;'>
                    • "MGNREGA में काम कैसे मिलेगा?"
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)