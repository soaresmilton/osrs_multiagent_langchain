from app.agents.tool_agent.schema import ToolAgentInput
from app.tools.templeosrs.service import TempleOsrsService

class ToolAgent:
    def __init__(self):
        self.service = TempleOsrsService()
    
    def run(self, input_data: ToolAgentInput) -> str:
        if input_data.tool_name == 'player_stats':
            result = self.service.get_player_stats(username=input_data.username)

        elif input_data.tool_name == 'player_info':
            result = self.service.get_player_info(username=input_data.username)
        
        else: 
            return "Unknown tool requested"
        

        if not result.success:
            return f"Error: {result.error}"
        
        return str(result.data)