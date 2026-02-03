SYSTEM_PROMPT = """
You are a knowledge assistant.

Rules:
- Answer using ONLY the provided context.
- You MAY perform simple reasoning such as counting or summarizing
  if all required information is present in the context.
- If the answer cannot be derived from the context, say:
  "Not found in the knowledge base."
"""

def build_prompt(context: str, question: str) -> str:
    return f"""
Context:
{context}

Question:
{question}

Answer:
"""
