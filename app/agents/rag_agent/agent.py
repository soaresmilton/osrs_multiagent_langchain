from app.agents.rag_agent.schema import RAGInput
from app.rag.retrieval.rag_chain import RAGChain

class RAGAgent:
    def __init__(self):
        self.chain = RAGChain()

    def run(self, input_data: RAGInput) -> str:
        return self.chain.run(question=input_data.question)
