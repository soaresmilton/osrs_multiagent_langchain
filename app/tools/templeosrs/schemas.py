from pydantic import BaseModel

class PlayerStatsInput(BaseModel):
    username: str
    date: int
    bosses: int

class PlayerInfoInput(BaseModel):
    username: str

class ToolResult(BaseModel):
    success: bool
    data: dict | None = None
    error: str | None = None    
