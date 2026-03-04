import requests
from app.config import OLLAMA_URL, MODEL_NAME

def generate_from_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception("LLM request failed")

    return response.json()["response"]