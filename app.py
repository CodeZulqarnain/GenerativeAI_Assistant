# app.py
import streamlit as st
from chat import chat_with_ai
import PyPDF2
import os
import json

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
st.title("🤖 AI Assistant with Documents & History")

HISTORY_FILE = "history.json"

# -----------------------------
# Load chat history if exists
# -----------------------------
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        st.session_state.messages = json.load(f)
else:
    st.session_state.messages = []

# -----------------------------
# Upload document
# -----------------------------
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
document_text = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            document_text += page.extract_text()
    else:  # TXT
        document_text = uploaded_file.read().decode("utf-8")
    st.success("Document uploaded successfully!")

# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User input
# -----------------------------
user_question = st.chat_input("Ask a question")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Prepare prompt
    if document_text:
        final_prompt = f"""
        Use the following document to answer the question.

        Document:
        {document_text}

        Question:
        {user_question}
        """
    else:
        final_prompt = user_question

    # Get AI response
    with st.spinner("Thinking..."):
        response = chat_with_ai(final_prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save persistent history
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)

# -----------------------------
# Clear chat button
# -----------------------------
if st.button("Clear Chat"):
    st.session_state.messages = []
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    st.stop()  # ✅ stops script and refreshes page
