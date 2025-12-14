# Government Schemes CHATBOT for Rural Empowerment

A comprehensive AI-powered chatbot designed to help rural and illiterate users access information about government schemes, policies, and benefits in their native language.

## Features

### Core Functionality
- **Multilingual Support**: Supports multiple Indian languages including Hindi, English, Bengali, Telugu, Marathi, Tamil, Gujarati, Kannada, Malayalam, and Punjabi
- **Speech Integration**: Voice input and output capabilities for illiterate users
- **RAG System**: Retrieval-Augmented Generation for accurate, contextual responses
- **Government Schemes Database**: Comprehensive knowledge base of Indian government schemes and policies

### Voice Features
- Speech-to-Text conversion in multiple Indian languages
- Text-to-Speech response generation
- Audio input recording and processing
- Language-specific voice recognition

### Government Schemes Coverage
- Agriculture schemes (PM-KISAN, etc.)
- Employment programs (MGNREGA)
- Health insurance (Ayushman Bharat)
- Housing schemes (PM Awas Yojana)
- Women welfare programs
- Education schemes
- Senior citizen benefits
- Banking and finance schemes

### User Experience
- Simple, accessible interface designed for rural users
- Large fonts and clear visual indicators
- Responsive design for mobile devices
- Emoji-rich responses for better understanding
- Category-based scheme exploration

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: HuggingFace Transformers
- **Vector Database**: FAISS
- **Speech Processing**: SpeechRecognition, gTTS
- **Translation**: Google Translate
- **Embeddings**: Sentence Transformers

## Project Structure

```
├── main.py                 # Main Streamlit application
├── config/
│   ├── settings.py         # Configuration settings
│   └── model_config.py     # ML model configurations
├── components/
│   ├── chatbot.py          # Main chatbot logic
│   ├── speech_handler.py   # Speech processing
│   ├── language_handler.py # Language support
|   ├── tts_handler.py      # Text-to-Speech handling
|   ├── llm_handler.py      # LLM support
│   └── ui_components.py    # UI components
├── data/
│   └── pdfs/
│       └── all pdfs        # Govt PDFs as the knowledge base
├── utils/
│   ├── text_processing.py  # Text utilities
│   └── helpers.py          # Helper functions
└── requirements.txt        # Dependencies
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and queries:
- Create an issue in the GitHub repository
- Contact the development team

## Acknowledgments

- HuggingFace for providing open-source models
- Indian Government for open data on schemes
- Streamlit community for the excellent framework
- Mentor and aquaintances for testing support

---

Built with ❤️ for rural India's digital empowerment
