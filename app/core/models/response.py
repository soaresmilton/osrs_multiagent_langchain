from pydantic import BaseModel
from typing import Literal

class AgentResponse(BaseModel):
    answer: str
    source: Literal["tool", "rag", "chat"]
    success: bool
