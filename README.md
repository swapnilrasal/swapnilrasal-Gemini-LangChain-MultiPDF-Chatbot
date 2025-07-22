# 📘 Gemini-LangChain MultiPDF Chatbot

> A powerful Streamlit application that lets you chat with your PDF documents using Google's Gemini-Pro AI via LangChain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Google AI](https://img.shields.io/badge/Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red.svg?style=for-the-badge)](https://github.com/swapnilrasal)

</div>

---

## 🌟 Features

<table>
<tr>
<td width="50%">

### 📄 Document Processing
- **PDF Upload** - Process PDF documents
- **Smart Text Extraction** - Advanced PDF parsing with PyPDF
- **Vector Embeddings** - Efficient semantic search with ChromaDB
- **Persistent Storage** - Cached embeddings for faster queries

</td>
<td width="50%">

### 🤖 AI-Powered Features
- **Intelligent Q&A** - Ask questions using Gemini-Pro
- **Auto Summaries** - Generate chapter-wise summaries
- **Key Concepts** - Extract important notes and definitions
- **Context-Aware** - Maintains conversation context

</td>
</tr>
</table>

---

## � Quick Start

### One-Click Setup ⚡

```bash
python3 setup_and_run.py
```

**That's it!** This command automatically:
- ✅ Checks your Python installation
- ✅ Creates and activates virtual environment
- ✅ Installs all dependencies
- ✅ Validates configuration
- ✅ Launches the app in your browser

---

## 📋 Prerequisites

| Requirement | Version | Download Link |
|-------------|---------|---------------|
| **Python** | 3.8+ | [Download](https://www.python.org/downloads/) |
| **Google API Key** | Free | [Get Key](https://makersuite.google.com/app/apikey) |
| **Git** | Latest | [Download](https://git-scm.com/downloads/) *(optional)* |

---

## 🛠️ Manual Installation

<details>
<summary><b>Click to expand manual setup instructions</b></summary>

### Step 1: Get the Code
```bash
git clone https://github.com/swapnilrasal/swapnilrasal-Gemini-LangChain-MultiPDF-Chatbot.git
cd swapnilrasal-Gemini-LangChain-MultiPDF-Chatbot
```

### Step 2: Create Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv && source venv/bin/activate

# Windows
python -m venv venv && venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create your free API key
3. Create `.env` file:
```bash
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

### Step 5: Launch App
```bash
streamlit run app.py
```

</details>

---

## 🎯 How to Use

### 1. 🚀 Launch the Application
Run `python3 setup_and_run.py` or `streamlit run app.py`

### 2. 📁 Upload Your PDFs
- Click **"Upload a textbook or PDF notes"**
- Select single PDF files
- Wait for processing completion

### 3. 💬 Ask Questions
- Type questions in the input field
- Get AI-powered answers instantly
- Ask follow-up questions for deeper insights

### 4. 📊 Generate Summaries
Expand **"Generate Summary & Notes"** for:
- **Unit/Chapter Summaries** - Structured overviews
- **Key Concepts** - Important definitions and points

---

## 📁 Project Structure

```
📦 swapnilrasal-Gemini-LangChain-MultiPDF-Chatbot
├── 🎯 app.py                 # Main Streamlit application
├── 📄 requirements.txt       # Python dependencies
├── � setup_and_run.py      # One-click setup script
├── 🔐 .env                  # API keys (keep secure!)
├── 🚫 .gitignore            # Git ignore rules
├── 📖 README.md             # This documentation
└── 📁 venv/                 # Virtual environment
```

---

## 🔧 Technology Stack

<div align="center">

| Component | Purpose | Documentation |
|-----------|---------|---------------|
| **Streamlit** | Web Interface | [Docs](https://docs.streamlit.io/) |
| **LangChain** | AI Framework | [Docs](https://python.langchain.com/) |
| **Google Gemini-Pro** | Language Model | [Docs](https://ai.google.dev/) |
| **ChromaDB** | Vector Database | [Docs](https://docs.trychroma.com/) |
| **PyPDF** | PDF Processing | [Docs](https://pypdf.readthedocs.io/) |

</div>

---

## 🚨 Troubleshooting

<details>
<summary><b>Common Issues & Solutions</b></summary>

### ❌ Module Not Found
```bash
source venv/bin/activate  # Activate environment
pip install -r requirements.txt
```

### ❌ API Key Issues
- Check `.env` file format: `GOOGLE_API_KEY=your_key`
- Verify API key is valid and has quota
- Remove any extra spaces or quotes

### ❌ Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### ❌ PDF Processing Errors
- Ensure PDFs contain text (not scanned images)
- Check files aren't password-protected
- Try smaller files first

### ❌ Virtual Environment Issues
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

</details>

---

## 🎨 Customization

<details>
<summary><b>Configuration Options</b></summary>

### Text Processing
```python
# In app.py
chunk_size = 1000        # Adjust for longer/shorter chunks
chunk_overlap = 200      # Increase for better context
```

### AI Model Settings
```python
temperature = 0.3        # Lower = more focused, Higher = more creative
model = "gemini-1.5-flash"  # Use different Gemini models
```

### UI Customization
- Modify Streamlit components in `app.py`
- Customize prompts for different response styles
- Add new summary generation options

</details>

---

## 🔒 Security & Privacy

- 🔐 API keys stored securely in `.env` file
- 🚫 Sensitive files excluded via `.gitignore`
- 🏠 All processing happens locally (except AI calls)
- 📝 No data stored on external servers

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. 🍴 Fork the repository
2. 🌿 Create feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Acknowledgments

<div align="center">

**Built with ❤️ using amazing open-source technologies**

[![Google AI](https://img.shields.io/badge/Google_AI-4285F4?style=flat&logo=google&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=flat&logo=database&logoColor=white)](https://www.trychroma.com/)

</div>

---

<div align="center">

**⭐ If this project helped you, please give it a star! ⭐**

</div> 
