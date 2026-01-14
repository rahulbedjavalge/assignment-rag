from assignment_rag.llm.openrouter import chat

if __name__ == "__main__":
    text, raw = chat(
        messages=[{"role": "user", "content": "Reply with exactly: pong"}],
        temperature=0.0,
        max_tokens=20,
    )
    print("Model reply:", text.strip())
    if raw.get("usage"):
        print("Usage:", raw["usage"])
