#convert raw doc into clean text
import os
import pdfplumber #extract text from pdf
from typing import List

'''Open the PDF
Loop through each page
Extract text safely (some pages may be empty)
Combine all pages into one string
Clean it before returning'''

def load_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return clean_text(text)



def load_txt(file_path: str) -> str:   #load_text
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return clean_text(text)

def clean_text(text: str) -> str: #remove newline/extra spaces
    return " ".join(text.split())

'''Scans the folder
Detects file type
Calls the appropriate loader
Returns a list of full documents as strings'''

def load_documents(folder_path: str) -> List[str]:
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".pdf"):
            documents.append(load_pdf(path))
        elif file.endswith(".txt"):
            documents.append(load_txt(path))

    return documents
