import faiss
import numpy as np
from typing import List

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.text_chunks = []

    def add(self, embeddings: np.ndarray, chunks: List[str]):
        self.index.add(embeddings)
        self.text_chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        top_k = min(top_k, len(self.text_chunks))
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            results.append({
                "chunk": self.text_chunks[idx],
                "distance": float(dist)
            })

        return results

