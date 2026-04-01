from app.agents.chat_agent.agent import ChatAgent
from app.agents.chat_agent.schema import ChatInput

def test_chat_agent_basic_response():
    agent = ChatAgent()
    result = agent.run(
        input_data=ChatInput(question="What is the best skill for making money in OSRS?")
    )

    assert isinstance(result, str)
    assert len(result) > 0

def test_chat_agent_no_player_data_fabrication():
    agent = ChatAgent()

    result = agent.run(
        input_data=ChatInput(question="What are my stats?")
    )

    normalized = result.lower()

    expected_phrases = [
        "do not have access",
        "don't have access",
        "cannot",
        "eu não tenho acesso",
        "eu não posso"
    ]

    assert any(p in normalized for p in expected_phrases)

    