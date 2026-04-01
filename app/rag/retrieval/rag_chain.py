from typing import List
from langchain_core.documents import Document
from langchain_core.messages import SystemMessage, HumanMessage

from app.core.models.llm import get_llm
from app.rag.retrieval.retriever import get_retriever
from app.rag.retrieval.vector_store import load_vectorstore
from app.agents.rag_agent.prompt import SYSTEM_PROMPT

class RAGChain:
    def __init__(self):
        self.llm = get_llm()
        self.vectorstore = load_vectorstore()
        self.retriever = get_retriever(self.vectorstore)

    def _build_context(self, documents: List[Document]) -> str:
        context_parts = []

        for i, doc in enumerate(documents):
            content = doc.page_content.strip()
            source = doc.metadata.get('file_name', 'unknown')

            context_parts.append(
                f"[Source {1 + i}] - {source}]\n{content}"
            )
        
        return "\n\n".join(context_parts)
    
    def run(self, question:str) -> str:
        documents: List[Document] = self.retriever.invoke(question)

        if not documents:
            return "I don't know"

        context = self._build_context(documents=documents)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"Context:\n{context}\n\nQuestion:\n{question}"
            )
        ]

        response = self.llm.invoke(messages)
        return response