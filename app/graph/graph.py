from langgraph.graph.state import CompiledStateGraph, StateGraph
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver


from app.graph.state import AgentState
from app.graph.nodes import (
    router_node,
    chat_node,
    rag_node,
    tool_node
)


checkpointer=InMemorySaver()

def build_graph() -> CompiledStateGraph:
    graph = StateGraph(AgentState)

    graph.add_node('router', router_node)
    graph.add_node('chat', chat_node)
    graph.add_node('rag', rag_node)
    graph.add_node('tool', tool_node)

    graph.set_entry_point('router')

    def route_decision(state: AgentState) -> str:
        return state['route']

    graph.add_conditional_edges(
        'router',
        route_decision,
        {
            'chat': 'chat',
            'rag': 'rag',
            'tool': 'tool'
        }
    )

    graph.add_edge('chat', END)
    graph.add_edge('rag', END)
    graph.add_edge('tool', END)

    return graph.compile()