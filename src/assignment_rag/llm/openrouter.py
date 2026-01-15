import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env from the project root
env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(env_path)

BASE_URL = "https://openrouter.ai/api/v1"

def chat(messages, model=None, temperature=0.2, max_tokens=300, timeout_s=60):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENROUTER_API_KEY in .env")

    model = model or os.getenv("OPENROUTER_MODEL")
    if not model:
        raise RuntimeError("Missing OPENROUTER_MODEL in .env")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": os.getenv("OPENROUTER_SITE_URL", "http://localhost"),
        "X-Title": os.getenv("OPENROUTER_APP_NAME", "AssignmentRAG"),
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    resp = requests.post(
        f"{BASE_URL}/chat/completions",
        headers=headers,
        json=payload,
        timeout=timeout_s,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"], data
