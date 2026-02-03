from ingestion.loaders import load_documents
from ingestion.chunker import chunk_text
from ingestion.embeddings import embed_texts, model
from retrieval.vector_store import VectorStore
from prompts.rag_prompt import SYSTEM_PROMPT, build_prompt
from llm import generate_answer

# 1. Load documents
docs = load_documents("data/raw_docs")

# 2. Chunk documents
all_chunks = []
for doc in docs:
    all_chunks.extend(chunk_text(doc))

print(f"Total chunks: {len(all_chunks)}")

# 3. Embed chunks
chunk_embeddings = embed_texts(all_chunks)

# 4. Vector store
dimension = chunk_embeddings.shape[1]
store = VectorStore(dimension)
store.add(chunk_embeddings, all_chunks)

# 5. Ask question
question = "What is the role of Associate Solution Support Engineer?"

# 6. Retrieve relevant chunks
query_embedding = model.encode([question])
retrieved_chunks = store.search(query_embedding, top_k=3)

context = "\n\n".join(retrieved_chunks)

# 7. Build prompt
user_prompt = build_prompt(context, question)

# 8. Generate answer using LLM
answer = generate_answer(SYSTEM_PROMPT, user_prompt)

print("\n🧠 ANSWER:\n")
print(answer)
