#Split large text into LLM-usable pieces
from typing import List

def chunk_text(text: str, chunk_size: int = 400, overlap: int = 80) -> List[str]:
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks

'''Start at index 0
Take 400 characters
Move forward, but step back 80 characters
Repeat until text ends'''

#Overlapping prevents loss and improves recall