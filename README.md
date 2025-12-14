# Multilingual Government Schemes RAG Chatbot

A comprehensive AI-powered chatbot designed to help rural and illiterate users access information about government schemes, policies, and benefits in their native language.

## Features

### 🎯 Core Functionality
- **Multilingual Support**: Supports 10+ Indian languages including Hindi, English, Bengali, Telugu, Marathi, Tamil, Gujarati, Kannada, Malayalam, and Punjabi
- **Speech Integration**: Voice input and output capabilities for illiterate users
- **RAG System**: Retrieval-Augmented Generation using HuggingFace models for accurate, contextual responses
- **Government Schemes Database**: Comprehensive knowledge base of Indian government schemes and policies
- **Form Filling Assistance**: Guides users through application processes

### 🗣️ Voice Features
- Speech-to-Text conversion in multiple Indian languages
- Text-to-Speech response generation
- Audio input recording and processing
- Language-specific voice recognition

### 🏛️ Government Schemes Coverage
- Agriculture schemes (PM-KISAN, etc.)
- Employment programs (MGNREGA)
- Health insurance (Ayushman Bharat)
- Housing schemes (PM Awas Yojana)
- Women welfare programs
- Education schemes
- Senior citizen benefits
- Banking and finance schemes

### 🎨 User Experience
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
│   ├── rag_system.py       # RAG implementation
│   ├── speech_handler.py   # Speech processing
│   ├── language_handler.py # Language support
│   └── ui_components.py    # UI components
├── data/
│   └── government_schemes.json # Schemes database
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

## Usage

### Text Interaction
1. Select your preferred language from the sidebar
2. Type your question about government schemes
3. Get detailed responses with scheme information, eligibility, and application process

### Voice Interaction
1. Click the "🎤 बोलकर पूछें" button
2. Speak your question in your chosen language
3. Receive both text and audio responses

### Scheme Categories
- Browse schemes by category using the sidebar
- Get suggested questions for common queries
- Access quick scheme information

## Key Features for Rural Users

### Accessibility
- **Simple Language**: Uses everyday language instead of technical jargon
- **Visual Indicators**: Clear icons and emojis for better understanding
- **Audio Support**: Complete voice interaction for illiterate users
- **Mobile Friendly**: Optimized for smartphones commonly used in rural areas

### Multilingual Support
- **Native Language Interface**: UI elements in user's preferred language
- **Automatic Translation**: Seamless translation between languages
- **Regional Language Support**: Covers major Indian languages
- **Cultural Context**: Responses adapted for rural Indian context

### Government Schemes Coverage
- **Comprehensive Database**: Covers major central and state schemes
- **Real-time Updates**: Regular updates to scheme information
- **Application Guidance**: Step-by-step application instructions
- **Document Requirements**: Clear list of required documents

## Model Architecture

### RAG System
- Uses multilingual sentence transformers for embeddings
- FAISS vector database for efficient similarity search
- Context-aware response generation
- Supports multiple languages with automatic translation

### Speech Processing
- Google Speech Recognition for multilingual STT
- Google Text-to-Speech for audio responses
- Audio file processing and playback
- Language-specific voice models

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a new Pull Request

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
- Contributors and testers from rural communities

---

Built with ❤️ for rural India's digital empowerment