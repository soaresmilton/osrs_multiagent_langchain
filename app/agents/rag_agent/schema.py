from pydantic import BaseModel

class RAGInput(BaseModel):
    question: str