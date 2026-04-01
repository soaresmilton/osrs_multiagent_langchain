from langchain_core.messages import SystemMessage, HumanMessage   

from app.core.models.llm import get_llm
from app.agents.chat_agent.prompt import SYSTEM_PROMPT
from app.agents.chat_agent.schema import ChatInput

from app.core.models.response import AgentResponse

class ChatAgent:
    def __init__(self):
        self.llm = get_llm()
    
    def run(self, input_data: ChatInput) -> AgentResponse:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=input_data.question)
        ]
        response = self.llm.invoke(messages)
        return AgentResponse(
            answer=response,
            source="chat",
            success=True
        )
