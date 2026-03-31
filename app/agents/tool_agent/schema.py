from pydantic import BaseModel

class ToolAgentInput(BaseModel):
    tool_name: str
    username: str