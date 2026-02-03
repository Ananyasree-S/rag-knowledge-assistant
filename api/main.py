from fastapi import FastAPI, UploadFile, File
import shutil
import os

from rag_pipeline import build_index, answer_question

app = FastAPI(title="RAG Knowledge Assistant")

UPLOAD_DIR = "data/raw_docs"

@app.on_event("startup")
def startup_event():
    build_index()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    build_index()
    return {"message": f"{file.filename} uploaded and indexed"}

@app.get("/query")
def query_knowledge(question: str):
    result = answer_question(question)
    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"]
    }

