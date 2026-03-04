from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.response_schema import JournalResponse
from app.services.analysis_service import analyze_journal
from app.utils.file_extractor import extract_text_from_upload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=JournalResponse)
async def analyze(request: Request):
    content = ""

    if request.headers.get("content-type", "").startswith("application/json"):
        data = await request.json()
        content = data.get("text", "")

    else:
        form = await request.form()
        text = form.get("text")
        file = form.get("file")

        if text:
            content += text

        if file:
            try:
                extracted_text = await extract_text_from_upload(file)
                content += "\n" + extracted_text
            except Exception as e:
                return {
                    "detectedThemes": ["Error"],
                    "sentiment": "Negative",
                    "goals": [
                        {
                            "category": "File Error",
                            "goal": str(e),
                            "priority": "Low"
                        }
                    ]
                }

    if not content.strip():
        return {
            "detectedThemes": ["Error"],
            "sentiment": "Negative",
            "goals": [
                {
                    "category": "Error",
                    "goal": "No text provided.",
                    "priority": "Low"
                }
            ]
        }

    return analyze_journal(content)