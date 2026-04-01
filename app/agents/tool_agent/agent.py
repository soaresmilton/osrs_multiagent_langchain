from app.agents.tool_agent.schema import ToolAgentInput
from app.tools.templeosrs.service import TempleOsrsService
from app.agents.tool_agent.selector import ToolSelector
from app.core.models.response import AgentResponse
from app.core.utils.parsing import extract_username_with_context

class ToolAgent:
    def __init__(self):
        self.service = TempleOsrsService()
        self.selector = ToolSelector()
    
    def run(self, input_data: ToolAgentInput, last_username: str | None = None) -> AgentResponse:
        question = input_data.question

        # 1 - Escolher tool:
        tool_name = self.selector.select(question)

        # 2 - extrair username
        username = last_username

        if not username: 
            return AgentResponse(
                answer="Could not identify username in your question.",
                source="tool",
                success= False
            )

        # 3 - Executar tool
        if tool_name == 'player_stats':
            result = self.service.get_player_stats(username=username)

        elif tool_name == 'player_info':
            result = self.service.get_player_info(username=username)
        
        else: 
            return "Unknown tool."
        

        if not result.success:
            return AgentResponse(
                answer={result.error},
                source="tool",
                success=False
            )
        
        # 5 -formatar a resposta
        return AgentResponse(
            answer=str(result.data),
            source="tool",
            success=True
        )