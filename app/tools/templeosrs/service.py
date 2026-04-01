from app.tools.templeosrs.client import TempleOsrsClient
from app.tools.templeosrs.schemas import ToolResult

class TempleOsrsService:
    def __init__(self, client=None):
        self.client = client or TempleOsrsClient() 
    
    def get_player_stats(self, username: str) -> ToolResult:
        try:
            data = self.client.get_player_stats(username=username)
            
            if not data:
                return ToolResult(
                    success=False,
                    error="Empty response from API"
                )
            
            return ToolResult(
                success=True,
                data=data
            )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Failed to fetch player stats: {str(e)}"
            )

    def get_player_info(self, username: str) -> ToolResult:
        try:
            data = self.client.get_player_info(username=username)

            if not data:
                return ToolResult(
                    success=False,
                    error="Empty response form API"
                )
            
            return ToolResult(
                success=True,
                data=data
            )
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Failed to fetch player infos: {str(e)}"
            )
