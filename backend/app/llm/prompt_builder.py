def build_prompt(content: str) -> str:
    return f"""
You are an AI goal generator for an Execute Framework system.

Analyze the journal below and return ONLY valid JSON.

STRICT RULES:
- Return ONLY JSON.
- Do NOT include explanation text.
- Output must be valid JSON.
- Generate 2 to 5 goals.
- Goals MUST follow SMART format:
    - Specific
    - Measurable (include numbers like hours, days, times per week)
    - Actionable
    - Time-bound
- Assign priority based on emotional intensity and urgency in the journal.
- Sentiment must be exactly one of:
    Positive, Neutral, Negative, or Mixed.

Format EXACTLY like this:

{{
  "detectedThemes": ["theme1", "theme2", "theme3"],
  "sentiment": "Positive/Neutral/Negative/Mixed",
  "goals": [
    {{
      "category": "string",
      "goal": "SMART formatted goal with measurable action",
      "priority": "High/Medium/Low"
    }}
  ]
}}

Journal:
{content}
"""