from langchain_core.messages import SystemMessage, HumanMessage   

from app.core.models.llm import get_llm
from app.agents.chat_agent.prompt import SYSTEM_PROMPT
from app.agents.chat_agent.schema import ChatInput

class ChatAgent:
    def __init__(self):
        self.llm = get_llm()
    
    def run(self, input_data: ChatInput) -> str:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=input_data.question)
        ]
        response = self.llm.invoke(messages)
        return response
