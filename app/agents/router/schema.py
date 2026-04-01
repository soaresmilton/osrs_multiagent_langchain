from pydantic import BaseModel
from enum import Enum

class Route(str, Enum):
    TOOL = "tool",
    RAG = "rag",
    CHAT = "chat"

class RouterInput(BaseModel):
    question: str