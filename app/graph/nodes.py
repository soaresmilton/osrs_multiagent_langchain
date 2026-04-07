from app.core.utils.parsing import extract_username_with_context
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
        ),
        history=state.get('history', [])
    )

    history = list(state.get('history', []))
    history.append(state['question'])


    return {
        **state, 
        "response":response.answer,
        "history": history
        }


def rag_node(state: TypedDict) -> TypedDict:
    response = rag_agent.run(
        RAGInput(
            question=state['question']
        )
    )

    history = list(state.get('history', []))
    history.append(state['question'])

    if not response.success:
        chat_result = chat_agent.run(
            ChatInput(question=state['question']),
            history=history
        )

        return {**state, "response": chat_result.answer, "history": history}
    
    return {**state, "response": response.answer, "history": history}

def tool_node(state: TypedDict) -> TypedDict:
    question = state['question']
    last_username = state.get('last_username')

    username = extract_username_with_context(
        question,
        last_username
    )

    response = tool_agent.run(
        ToolAgentInput(
            question=question
        ),
        last_username=username
        
    )

    history = list(state.get('history', []))
    history.append(question)

    if not response.success:
        return {
            **state,
            "response": f"Tool error: {response.answer}"
        }

    return {
        **state, 
        "response": response.answer, 
        "last_username": username, 
        "history": history
    }