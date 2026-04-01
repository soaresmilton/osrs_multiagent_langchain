from typing import Literal

ToolName = Literal["player_stats", "player_info"]

class ToolSelector:
    def select(self, question: str) -> ToolName:
        q = question.lower()

        if "stat" in q or "level" in q or "stats" in q:
            return "player_stats"

        if "account" in q or "info" in q or "information" in q:
            return "player_info"

        
        return "player_stats"