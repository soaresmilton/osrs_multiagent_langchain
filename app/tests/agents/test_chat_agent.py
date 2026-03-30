from app.agents.chat_agent.agent import ChatAgent
from app.agents.chat_agent.schema import ChatInput

def test_chat_agent_basic_response():
    agent = ChatAgent
    result = agent.run(
        ChatInput(question="What is the best skill for making money in OSRS?")
    )

    assert isinstance(result, str)
    assert len(result) > 0

def test_chat_agent_no_player_data_fabrication():
    agent = ChatAgent()

    result = agent.run(
        ChatInput(question="What are my stats?")
    )

    assert "don't have access" in result.lower() or "cannot" in result.lower()

    