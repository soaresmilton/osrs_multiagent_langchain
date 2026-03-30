from pydantic import BaseModel, Field

class ChatInput(BaseModel):
    question: str = Field(description="User question")
