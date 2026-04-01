from app.agents.rag_agent.agent import RAGAgent
from app.agents.rag_agent.schema import RAGInput

def test_rag_returns_answer():
    agent = RAGAgent()

    result = agent.run(
        RAGInput(question="Qual principal trama por trás da quest Song of The Elves?")
    )

    assert isinstance(result, str)
    assert len(result) > 0

def test_rag_unknow_question():
    agent = RAGAgent()
    
    result = agent.run(
    RAGInput(question="Qual capital do Brasil?")
    )

    normalized = result.lower()
    expected_phrases = ["i don't know", "i does not know", "eu não sei", "não sei"]

    assert any(phrase in normalized for phrase in expected_phrases)