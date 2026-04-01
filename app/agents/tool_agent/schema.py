from pydantic import BaseModel

class ToolAgentInput(BaseModel):
    question: str