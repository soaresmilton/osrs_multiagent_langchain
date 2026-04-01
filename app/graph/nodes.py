from typing import TypedDict

from app.agents.router.agent import RouterAgent
from app.agents.router.schema import RouterInput

from app.agents.chat_agent.agent import ChatAgent
from app.agents.chat_agent.schema import ChatInput

from app.agents.rag_agent.agent import RAGAgent
from app.agents.rag_agent.schema import RAGInput

from app.agents.tool_agent.agent import ToolAgent
from app.agents.tool_agent.schema import ToolAgentInput

from app.core.utils.parsing import extract_username

router = RouterAgent()
chat_agent = ChatAgent()
rag_agent = RAGAgent()
tool_agent = ToolAgent()


def router_node(state: TypedDict) -> TypedDict:
    route = router.run(
        RouterInput(
            question=state['question']
        )
    )

    return {**state, "route": route.value}

def chat_node(state: TypedDict) -> TypedDict:
    response = chat_agent.run(
        ChatInput(
            question=state['question']
        )
    )

    return {**state, "response":response}


def rag_node(state: TypedDict) -> TypedDict:
    response = rag_agent.run(
        RAGInput(
            question=state['question']
        )
    )

    return {**state, "response": response}


def tool_node(state: TypedDict) -> TypedDict:

    question = state['question']
    username = extract_username(question)

    if not username:
        return {
            **state,
            "response": "Could not identify username in your question."
        }
    
    response = tool_agent.run(
        ToolAgentInput(
            tool_name="player_stats",
            username=username
        )
    )

    return {**state, "response": response}