import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="RAG Knowledge Assistant", layout="centered")

st.title("🧠 RAG Knowledge Assistant")
st.write("Ask questions from uploaded internal documents")

# -------------------------------
# Upload Section
# -------------------------------
st.header("📂 Upload Document")

uploaded_file = st.file_uploader(
    "Upload a PDF or TXT file",
    type=["pdf", "txt"]
)

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post(f"{API_BASE_URL}/upload", files=files)

    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to upload document")

# -------------------------------
# Query Section
# -------------------------------
st.header("💬 Ask a Question")

question = st.text_input(
    "Enter your question",
    placeholder="What is the role of Associate Solution Support Engineer?"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            response = requests.get(
                f"{API_BASE_URL}/query",
                params={"question": question}
            )

        if response.status_code == 200:
            answer = response.json()["answer"]

            st.subheader("🧠 Answer")
            st.write(answer)
        else:
            st.error("Failed to get answer")
