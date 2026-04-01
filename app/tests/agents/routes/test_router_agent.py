from app.agents.router.agent import RouterAgent
from app.agents.router.schema import RouterInput, Route

def test_router_tool():
    router = RouterAgent()
    result = router.run(
        RouterInput(
            question="What are the stats of player Zeah?"
        )
    )

    assert result == Route.TOOL


def test_router_rag():
    router = RouterAgent()

    result = router.run(
        RouterInput(
            question="What do I complete Dragon Slayer II?"
        )
    )

    assert result == Route.RAG


def test_router_chat(mocker):
    router = RouterAgent()

    mocker.patch.object(
        router.classifier,
        "classify",
        return_value="chat"
    )

    result = router.run(
        RouterInput(
            question="What is the best skill for money?"
        )
    )

    assert result == Route.CHAT

