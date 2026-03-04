from pydantic import BaseModel

class JournalRequest(BaseModel):
    text: str