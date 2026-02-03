from ingestion.loaders import load_documents
from ingestion.chunker import chunk_text
from ingestion.embeddings import embed_texts, model
from retrieval.vector_store import VectorStore
from prompts.rag_prompt import SYSTEM_PROMPT, build_prompt
from llm import generate_answer

vector_store = None
index_built = False

# Global objects (loaded once)
vector_store = None

def build_index(doc_folder="data/raw_docs"):
    global vector_store, index_built

    if index_built:
        return  # 🚀 cache hit

    docs = load_documents(doc_folder)

    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_text(doc))

    embeddings = embed_texts(all_chunks)

    dimension = embeddings.shape[1]
    vector_store = VectorStore(dimension)
    vector_store.add(embeddings, all_chunks)

    index_built = True

def answer_question(question: str):
    if vector_store is None:
        return {
            "answer": "Knowledge base not initialized.",
            "sources": []
        }

    query_embedding = model.encode([question])
    results = vector_store.search(query_embedding, top_k=3)

    # similarity threshold (tune later)
    if results[0]["distance"] > 1.2:
        return {
            "answer": "Not found in the knowledge base.",
            "sources": []
        }

    context = "\n\n".join(r["chunk"] for r in results)
    user_prompt = build_prompt(context, question)

    answer = generate_answer(SYSTEM_PROMPT, user_prompt)

    sources = [
        f"Chunk {i+1}" for i in range(len(results))
    ]

    return {
        "answer": answer,
        "sources": sources
    }

