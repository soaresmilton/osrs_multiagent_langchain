import re
from typing import Optional
from app.core.models.llm import get_llm

def extract_username(question: str) -> Optional[str]:
    """
    Try to extract OSRS username from user question.
    """
    patters = [
        r"player\s+([a-zA-Z0-9_ ]+)",
        r"stats\s+of\s+([a-zA-Z0-9_ ]+)",
        r"for\s+([a-zA-Z0-9_ ]+)"
    ]

    for pattern in patters:
        match = re.search(pattern, question, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return _extract_with_llm(question)


def _extract_with_llm(question: str) -> Optional[str]:
    llm = get_llm()
    prompt = f"""
Extract the OSRS username from the question.

Rules:
- Return ONLY the username
- If no username is present, return NONE

Question:
{question}
"""
    response = llm.invoke(prompt)

    result = response.strip()

    if result.upper() == 'NONE':
        return None
    
    return result

def extract_username_with_context(
    question: str,
    last_username: Optional[str]
) -> Optional[str]:
    username = extract_username(question)

    if username:
        return username

    return last_username