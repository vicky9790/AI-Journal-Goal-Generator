from pydantic import BaseModel
from typing import List

class Goal(BaseModel):
    category: str
    goal: str
    priority: str

class JournalResponse(BaseModel):
    detectedThemes: List[str]
    sentiment: str
    goals: List[Goal]