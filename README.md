# 📘 Gemini-LangChain-MultiPDF-Chatbot

A polished Streamlit app for uploading multiple PDFs and asking questions with Gemini‑Pro via LangChain.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

- 📄 **Multiple PDF Upload**: Upload and process multiple PDF files simultaneously
- 🤖 **AI-Powered Q&A**: Ask questions about your documents using Google's Gemini-Pro
- 📚 **Smart Summaries**: Generate unit/chapter-wise summaries automatically
- 📝 **Important Notes**: Extract key concepts, definitions, and important points
- 🔍 **Vector Search**: Advanced semantic search with ChromaDB embeddings
- 💾 **Persistent Storage**: Cached embeddings for faster subsequent queries
- 🎨 **User-Friendly Interface**: Clean and intuitive Streamlit interface

## 🛠️ Quick Start

### One-Click Setup (Recommended)

```bash
python3 setup_and_run.py
```

This single command will:
- ✅ Create virtual environment
- ✅ Install all dependencies  
- ✅ Validate configuration
- ✅ Launch the app automatically

### Manual Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd swapnilrasal-Gemini-LangChain-MultiPDF-Chatbot
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Get your Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file:
     ```
     GOOGLE_API_KEY=your_actual_google_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Internet connection for initial package downloads

## 🎯 How to Use

1. **Start the Application**: Use one of the automated setup scripts above
2. **Upload PDFs**: Click "Upload a textbook or PDF notes" and select your PDF files
3. **Ask Questions**: Type your questions in the text input field
4. **Generate Summaries**: Use the expandable section to create structured notes
5. **Extract Key Points**: Get important concepts and definitions automatically

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── requirements.txt       # Essential Python dependencies (9 packages)
├── setup_and_run.py      # One-click setup and run script
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🔧 Core Dependencies (9 Essential Packages)

- **streamlit**: Web application framework
- **langchain**: AI application development framework  
- **langchain-google-genai**: Gemini-Pro integration
- **langchain-community**: Community document loaders
- **langchain-text-splitters**: Text processing utilities
- **pypdf**: PDF text extraction
- **python-dotenv**: Environment variable management
- **chromadb**: Vector database for embeddings
- **watchdog**: Optional performance enhancement

## 🚨 Troubleshooting

### Common Issues:

1. **Import Errors**: The automated scripts handle dependency conflicts
2. **API Key Issues**: Ensure your Google API key is valid and properly set in `.env`
3. **Virtual Environment**: The scripts automatically create and manage virtual environments
4. **Port Already in Use**: If port 8501 is busy, Streamlit will automatically use the next available port

### Getting Help:

- Check the terminal output for detailed error messages
- Ensure you have a stable internet connection
- Verify your Google API key is active and has sufficient quota

## 🎨 Customization

You can customize the application by modifying:
- **Chunk size**: Adjust `chunk_size` and `chunk_overlap` in `app.py`
- **Model settings**: Change the Gemini model or temperature
- **UI elements**: Modify Streamlit components and styling
- **Prompts**: Customize the AI prompts for better responses

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⭐ Acknowledgments

- Google AI for Gemini-Pro API
- LangChain community for the amazing framework
- Streamlit team for the excellent web framework
# swapnilrasal-Gemini-LangChain-MultiPDF-Chatbot
A polished Streamlit app for uploading multiple PDFs and asking questions with Gemini‑Pro via LangChain 
