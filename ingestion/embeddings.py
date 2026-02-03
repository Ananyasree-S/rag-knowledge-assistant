#Convert human language → numerical vectors that capture meaning.
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

print("🔄 Loading embedding model (first run may take a minute)...")
model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Embedding model loaded")

def embed_texts(texts: List[str]) -> np.ndarray:
    print(f"🔢 Generating embeddings for {len(texts)} chunks...")
    embeddings = model.encode(texts, show_progress_bar=True)
    return np.array(embeddings)
