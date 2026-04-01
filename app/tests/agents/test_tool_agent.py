from app.agents.tool_agent.agent import ToolAgent
from app.agents.tool_agent.schema import ToolAgentInput

def test_tool_agent_stats(mocker):
    mock_service = mocker.Mock()

    mock_service.get_player_stats.return_value.success = True
    mock_service.get_player_stats.return_value.data = {
        "Overall_level": 2376
    }

    agent = ToolAgent()
    agent.service = mock_service

    mocker.patch(
        "app.core.utils.parsing.extract_username",
        return_value="Hoom Pk"
    )

    mocker.patch.object(
        agent.selector,
        "select",
        return_value="player_stats"
    )

    result = agent.run(
        ToolAgentInput(question="stats of Hoom Pk")
    )

    assert "2376" in result

    mock_service.get_player_stats.assert_called_once_with(username='Hoom Pk')