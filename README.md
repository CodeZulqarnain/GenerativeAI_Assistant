# GenerativeAI_Assistant

A web-based AI Assistant with **PDF/TXT document support**, **chat history**, and **RAG (Retrieval-Augmented Generation)** functionality built with **Groq LLaMA 3.1** and **Streamlit**.

---

## Features

- Chat with **persistent history**  
- Upload **PDF** and **TXT** documents for context-aware answers  
- Clear chat anytime  
- Retrieval-Augmented Generation (RAG) using uploaded documents  
- Built with **Streamlit** for an interactive web interface  
- Uses **Groq LLaMA 3.1 API** (free tier)

---

## Project Structure

GenerativeAI_Assistant/
├── app.py # Main Streamlit app
├── chat.py # Groq API interaction
├── requirements.txt # Python dependencies
└── history.json # Optional file for storing chat history


---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/USERNAME/GenerativeAI_Assistant.git
cd GenerativeAI_Assistant
Install dependencies

pip install -r requirements.txt
Set your Groq API key

Windows:
set GROQ_API_KEY=gsk_your_api_key_here
Mac/Linux:
export GROQ_API_KEY=gsk_your_api_key_here
Run the App Locally
python -m streamlit run app.py
Upload PDF or TXT

Ask questions

Chat history persists until cleared

Deployment
Push the project to GitHub

Deploy on Streamlit Cloud

Set GROQ_API_KEY as a secret on Streamlit Cloud

Your app is now accessible online via a public URL

How it Works
User enters a question in the chat box

If a document is uploaded:

The app extracts text from PDF/TXT

Combines user question + document text

Sends to Groq LLaMA 3.1 API for answer

AI response is displayed in the chat

Chat history is saved locally (history.json)

Clear chat button resets conversation

Technologies Used
Streamlit – Web interface

PyPDF2 – PDF text extraction

Groq LLaMA 3.1 – AI model

Python 3.11 – Programming language

Optional Enhancements
Document chunking + vector embeddings for large PDFs

Support for image/OCR input

Enhanced UI/UX with colors and instructions

Author
Zulqarnain Mohi Ud Din 
