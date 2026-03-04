from app.llm.prompt_builder import build_prompt
from app.llm.ollama_client import generate_from_llm
from app.utils.json_parser import extract_json

def analyze_journal(text: str):
    prompt = build_prompt(text)
    raw_output = generate_from_llm(prompt)
    structured_output = extract_json(raw_output)
    return structured_output
    
