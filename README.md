# RAG-based Knowledge Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that answers
user queries using custom documents instead of relying solely on LLM memory.

## Features
- Document ingestion and chunking
- Vector embeddings using FAISS
- Semantic search for relevant context
- LLM-powered answer generation
- REST API using FastAPI

## Tech Stack
- Python
- FastAPI
- FAISS
- OpenAI / HuggingFace embeddings

## Architecture
1. Documents are chunked and embedded
2. Stored in a vector database
3. User query is embedded
4. Top-k relevant chunks retrieved
5. LLM generates grounded response

## How to Run
```bash
pip install -r requirements.txt
python backend/app.py
