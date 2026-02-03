import ollama

def generate_answer(system_prompt: str, user_prompt: str) -> str:
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response["message"]["content"].strip()
