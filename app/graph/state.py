from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    question: str
    route: Optional[str]
    response: Optional[str]
    history: List[str]
    last_username: Optional[str]
