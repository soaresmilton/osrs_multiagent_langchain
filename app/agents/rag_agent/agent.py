from app.agents.rag_agent.schema import RAGInput
from app.rag.retrieval.rag_chain import RAGChain

from app.core.models.response import AgentResponse

class RAGAgent:
    def __init__(self):
        self.chain = RAGChain()

    def run(self, input_data: RAGInput) -> AgentResponse:
        result = self.chain.run(question=input_data.question)
        success = "don't know" not in result.lower()
        return AgentResponse(
            answer=result,
            source="rag",
            success=success
        )
