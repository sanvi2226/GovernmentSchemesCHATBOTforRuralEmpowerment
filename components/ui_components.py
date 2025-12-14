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
       MODERN SIDEBAR WITH CARDS
       ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f5f7f0 100%);
        border-right: 3px solid var(--accent-green);
        padding: 1.5rem 1rem;
    }
    
    [data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    
    [data-testid="stSidebar"] h3 {
        color: var(--primary-green);
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid var(--accent-green);
    }
    
    /* Sidebar category cards */
    .sidebar-card {
        background: linear-gradient(135deg, #ffffff 0%, #f1f8f4 100%);
        border: 2px solid var(--accent-green);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.75rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(46, 125, 50, 0.1);
    }
    
    .sidebar-card:hover {
        background: linear-gradient(135deg, #e8f5e9 0%, #f1f8f4 100%);
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.2);
        border-color: var(--primary-green);
    }
    
    .sidebar-card-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .sidebar-card-title {
        color: var(--primary-green);
        font-weight: 600;
        font-size: 1rem;
        margin: 0.5rem 0 0.3rem 0;
    }
    
    .sidebar-card-desc {
        color: var(--text-medium);
        font-size: 0.85rem;
        line-height: 1.4;
        margin: 0;
    }
    
    /* Refresh button styling */
    .refresh-button,
    [data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, var(--primary-green), var(--light-green)) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        margin-bottom: 1.5rem !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 3px 10px rgba(46, 125, 50, 0.3) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] .stButton button:hover,
    .refresh-button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.4) !important;
    }
    
    /* Tip box in sidebar */
    .sidebar-tip {
        background: linear-gradient(135deg, #e8f5e9, #fff9c4);
        padding: 1rem;
        border-radius: 15px;
        border-left: 4px solid var(--primary-green);
        margin-top: 1.5rem;
        box-shadow: 0 2px 8px rgba(46, 125, 50, 0.1);
    }
    
    .sidebar-tip-title {
        color: var(--primary-green);
        font-weight: 600;
        margin: 0 0 0.5rem 0;
        font-size: 1rem;
    }
    
    .sidebar-tip-text {
        color: var(--text-medium);
        font-size: 0.9rem;
        margin: 0;
        line-height: 1.5;
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
       IMPROVED CHAT INPUT BOX - FIX ALL ISSUES
       ============================================ */
    /* Fix background gap - ensure gradient covers everything */
    .main {
        background: linear-gradient(135deg, #f5f7f0 0%, #e8f5e9 50%, #fff8e1 100%) !important;
        background-attachment: fixed !important;
        min-height: 100vh !important;
    }
    
    /* Remove any fixed positioning or bottom constraints */
    [data-testid="stBottom"] {
        position: relative !important;
        bottom: auto !important;
        padding: 1rem 0 2rem 0 !important;
        background: transparent !important;
        width: 100% !important;
        max-width: 100% !important;
    }
    
    .stChatFloatingInputContainer {
        position: relative !important;
        bottom: auto !important;
        background: transparent !important;
        padding: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
    }
    
    [data-testid="stChatInput"] {
        background: white !important;
        border-radius: 30px !important;
        padding: 0.5rem 0.5rem 0.5rem 1.5rem !important;
        box-shadow: 0 4px 20px var(--shadow-strong) !important;
        border: 3px solid var(--accent-green) !important;
        margin: 1rem auto !important;
        width: 100% !important;
        max-width: 100% !important;
        position: relative !important;
        display: flex !important;
        align-items: center !important;
    }
    
    [data-testid="stChatInput"] > div {
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.5rem !important;
    }
    
    [data-testid="stChatInput"] textarea {
        font-size: 1.05rem !important;
        line-height: 1.6 !important;
        padding: 1rem 0.5rem !important;
        border: none !important;
        color: var(--text-dark) !important;
        min-height: 24px !important;
        max-height: 150px !important;
        background: transparent !important;
        width: 100% !important;
        overflow-y: auto !important;
        resize: none !important;
        flex: 1 !important;
    }
    
    [data-testid="stChatInput"] textarea::placeholder {
        color: var(--text-medium) !important;
        opacity: 0.7 !important;
        font-size: 1rem !important;
    }
    
    [data-testid="stChatInput"] textarea:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    
    /* Fix send button - use simple arrow, no cutting */
    [data-testid="stChatInput"] button {
        background: linear-gradient(135deg, var(--primary-green), var(--light-green)) !important;
        color: white !important;
        border-radius: 50% !important;
        padding: 0 !important;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 3px 10px rgba(46, 125, 50, 0.3) !important;
        width: 48px !important;
        height: 48px !important;
        min-width: 48px !important;
        min-height: 48px !important;
        flex-shrink: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
    }
    
    [data-testid="stChatInput"] button:hover {
        transform: scale(1.08) !important;
        box-shadow: 0 4px 16px rgba(46, 125, 50, 0.5) !important;
    }
    
    [data-testid="stChatInput"] button:active {
        transform: scale(0.95) !important;
    }
    
    /* Style the button icon */
    [data-testid="stChatInput"] button svg {
        width: 24px !important;
        height: 24px !important;
        fill: white !important;
    }
    
    /* Ensure input container doesn't get cut off */
    .main .block-container {
        padding-bottom: 6rem !important;
        background: transparent !important;
    }
    
    /* Fix any white gaps */
    [data-testid="stVerticalBlock"],
    [data-testid="column"],
    .element-container {
        background: transparent !important;
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
    
    /* Audio input button styling */
    button[data-testid="baseButton-secondary"] {
        background: linear-gradient(135deg, #ff6b6b, #ee5a6f) !important;
        color: white !important;
        border-radius: 50% !important;
        width: 56px !important;
        height: 56px !important;
        min-width: 56px !important;
        min-height: 56px !important;
        font-size: 1.8rem !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
        margin-bottom: 1rem !important;
        border: none !important;
    }
    
    button[data-testid="baseButton-secondary"]:hover {
        background: linear-gradient(135deg, #ee5a6f, #ff6b6b) !important;
        transform: scale(1.1) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.5) !important;
    }
    
    /* Language selector styling */
    [data-testid="stSidebar"] .stSelectbox {
        margin-bottom: 1.5rem;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background: white;
        border: 2px solid var(--accent-green);
        border-radius: 12px;
        padding: 0.5rem;
        font-weight: 500;
        color: var(--text-dark);
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: var(--primary-green);
        font-weight: 600;
        font-size: 0.95rem;
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
        
        .sidebar-card {
            padding: 0.75rem;
        }
        
        .sidebar-card-icon {
            font-size: 1.5rem;
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
                
    /* ============================================
   SIMPLE CLEAN INPUT BAR (Just like your sample)
   ============================================ */
[data-testid="stChatInput"] {
    background: #ffffff !important;
    border: 2px solid #7EC27E !important;
    border-radius: 40px !important;
    padding: 0.4rem 1rem !important;
    box-shadow: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.5rem !important;
    height: 52px !important;
}

/* Clean text area */
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    font-size: 1rem !important;
    padding: 0 !important;
    margin: 0 !important;
    height: 32px !important;
    line-height: 32px !important;
}

/* Clean send button */
[data-testid="stChatInput"] button {
    background: #2e7d32 !important;
    border-radius: 50% !important;
    width: 40px !important;
    height: 40px !important;
    min-width: 40px !important;
    min-height: 40px !important;
    padding: 0 !important;
    box-shadow: none !important;
}

/* ============================================
   FIX MIC BUTTON — align in same horizontal line
   ============================================ */
button[key="audio_input"] {
    background: #ffffff !important;
    border: 2px solid #7EC27E !important;
    border-radius: 50% !important;
    width: 48px !important;
    height: 48px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: none !important;
    margin-top: 4px !important;
}

/* mic should NOT float */
[data-testid="column"]:nth-child(1) {
    display: flex !important;
    align-items: center !important;
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
    """Render enhanced sidebar with modern card structure"""
    
    # Language Selection Header
    st.sidebar.markdown("""
        <div style='background: linear-gradient(135deg, #e8f5e9, #c8e6c9); 
                    padding: 1rem; border-radius: 12px; 
                    border: 2px solid #81c784; margin-bottom: 1rem;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);'>
            <h4 style='color: #1b5e20; margin: 0; font-size: 1.1rem;
                       display: flex; align-items: center; gap: 0.5rem;'>
                🌐 <span>Select Language / भाषा चुनें</span>
            </h4>
        </div>
    """, unsafe_allow_html=True)
    
    from components.language_handler import LanguageHandler
    
    # Most used languages for rural India
    languages = [
        ('hi', 'हिन्दी (Hindi)'),
        ('en', 'English'),
        ('bn', 'বাংলা (Bengali)'),
        ('te', 'తెలుగు (Telugu)'),
        ('mr', 'मराठी (Marathi)'),
        ('ta', 'தமிழ் (Tamil)'),
        ('gu', 'ગુજરાતી (Gujarati)'),
        ('kn', 'ಕನ್ನಡ (Kannada)')
    ]
    
    # Radio buttons with clear visibility
    selected_language = st.sidebar.radio(
        "Select:",
        options=[code for code, name in languages],
        format_func=lambda x: dict(languages)[x],
        index=0,  # Default Hindi
        key="selected_language",
        label_visibility="collapsed"
    )
    
    # Show current selection prominently
    selected_name = dict(languages)[selected_language]
    st.sidebar.markdown(f"""
        <div style='background: #fff9c4; padding: 0.75rem; 
                    border-radius: 8px; margin: 1rem 0;
                    border: 2px solid #f9a825; text-align: center;'>
            <div style='color: #f57f17; font-size: 0.85rem; font-weight: 600;'>
                CURRENTLY SELECTED
            </div>
            <div style='color: #000; font-size: 1.1rem; font-weight: 700; margin-top: 0.25rem;'>
                {selected_name}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("### 📚 Scheme Categories")
    
    # Rest of your sidebar code...
    categories = [
        ("🌾", "Agriculture & Farming", "PM-KISAN, Crop Insurance"),
        ("🏥", "Health & Welfare", "Ayushman Bharat"),
        ("🏠", "Housing", "PM Awas Yojana"),
        ("💼", "Employment", "MGNREGA"),
        ("👨‍👩‍👧", "Social Welfare", "Pension Schemes"),
        ("📚", "Education", "Scholarships")
    ]
    
    for icon, title, desc in categories:
        st.sidebar.markdown(f"""
        <div class="sidebar-card">
            <span class="sidebar-card-icon">{icon}</span>
            <div class="sidebar-card-title">{title}</div>
            <div class="sidebar-card-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div class="sidebar-tip">
        <div class="sidebar-tip-title">💡 Pro Tip</div>
        <div class="sidebar-tip-text">
            Speak or type in your language! 🎤
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_chat_interface(chatbot):
    """Render the main chat interface with enhanced styling"""
    from components.language_handler import LanguageHandler
    import speech_recognition as sr
    
    # Initialize language handler
    if 'language_handler' not in st.session_state:
        st.session_state.language_handler = LanguageHandler()
    
    # Get selected language from session state
    selected_lang = st.session_state.get('selected_language', 'hi')
    
    # Chat messages container
    chat_container = st.container()
    
    with chat_container:
        # Display chat messages with audio (UPDATED LOOP)
        for idx, message in enumerate(st.session_state.messages):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
                # Add audio player for assistant messages (NEW CODE BLOCK)
                if message["role"] == "assistant":
                    audio_key = f"audio_{idx}"
                    
                    if audio_key not in st.session_state:
                        # Generate audio for this response
                        audio_path = st.session_state.tts_handler.text_to_speech(
                            message["content"],
                            language=selected_lang,
                            filename=f"response_{idx}.mp3"
                        )
                        st.session_state[audio_key] = audio_path
                    else:
                        audio_path = st.session_state[audio_key]
                    
                    # Display audio player if audio was generated successfully
                    if audio_path and audio_path.exists():
                        st.markdown("""
                            <div class="audio-player-container">
                                <div class="audio-icon">🔊</div>
                                <div class="audio-text">
                                    <div class="audio-title">Listen to Response / जवाब सुनें</div>
                                    <div class="audio-subtitle">Click play to hear the answer</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Display audio player
                        st.audio(str(audio_path), format='audio/mp3')
    
    # Create columns for audio input button and text input
    col1, col2 = st.columns([1, 12], vertical_alignment="center")

    
    with col1:
        # Audio input button
        if st.button("🎤", key="audio_input", help="Click to speak", type="secondary"):
            with st.spinner("🎙️ Listening... Please speak now"):
                try:
                    recognizer = sr.Recognizer()
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    
                    # Recognize speech in selected language
                    recognized_text = st.session_state.language_handler.recognize_speech(
                        audio, 
                        selected_lang
                    )
                    
                    if recognized_text:
                        # Process the recognized text
                        st.session_state.messages.append({"role": "user", "content": recognized_text})
                        
                        with st.spinner("🔍 Analyzing documents and preparing answer..."):
                            # Translate query to English for processing
                            query_en = st.session_state.language_handler.translate_text(
                                recognized_text, 
                                source_lang=selected_lang, 
                                target_lang='en'
                            )
                            
                            # Get response from chatbot
                            response_en = chatbot.generate_answer(query_en)
                            
                            # Translate response back to selected language
                            response = st.session_state.language_handler.translate_text(
                                response_en,
                                source_lang='en',
                                target_lang=selected_lang
                            )
                        
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
                    else:
                        st.error("❌ Could not understand audio. Please try again or type your question.")
                        
                except sr.WaitTimeoutError:
                    st.error("⏱️ No speech detected. Please try again.")
                except Exception as e:
                    st.error(f"🔇 Microphone error: Please check permissions or type your question.")
    
    with col2:
        # Input section with enhanced prompt
        prompt = st.chat_input("💬 अपना सवाल यहाँ लिखें | Type your question here...")
    
    if prompt:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("🔍 Analyzing documents and preparing answer..."):
            # Translate query to English for processing
            query_en = st.session_state.language_handler.translate_text(
                prompt,
                source_lang=selected_lang,
                target_lang='en'
            )
            
            # Get response from chatbot
            response_en = chatbot.generate_answer(query_en)
            
            # Translate response back to selected language
            response = st.session_state.language_handler.translate_text(
                response_en,
                source_lang='en',
                target_lang=selected_lang
            )
        
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