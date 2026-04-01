from app.core.models.llm import get_llm


TOOL_KEYWORDS = ["stats", "player", "level", "account"]
RAG_LEYWORDS = ["quest", "guide", "grandmaster", "lore"]

class RouterClassifier:
    def __init__(self):
        self.llm = get_llm()

    def _rule_base(self, question: str) -> str | None:
        q = question.lower()

        if any(k in q for k in TOOL_KEYWORDS):
            return "tool"
        if any(k in q for k in RAG_LEYWORDS):
            return "rag"

        return None
    
    def _llm_based(self, question: str) -> str:
        prompt = f"""
Classify the user question into one of the following categories:

- tool → if it requires player-specific data
- rag → if it is about quests or guides
- chat → general questions

Respond ONLY with one word: tool, rag, or chat.

Question:
{question}
"""

        response = self.llm.invoke(prompt)

        return response.content.strip.lower()
    
    def classify(self, question: str) -> str:
        rule_result = self._rule_base(question)

        if rule_result:
            return rule_result

        return self._llm_based(question)