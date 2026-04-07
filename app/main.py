from app.graph.graph import build_graph
from app.core.memory.memory_store import MemoryStore
import uuid

def main():
    graph = build_graph()
    memory = MemoryStore()

    user_input = input('Enter session ID or press ENTER for new: ')

    if user_input.strip():
        session_id = user_input
    else:
        session_id = str(uuid.uuid4())

    print(f"Session ID:{session_id} ")

    state = memory.load(session_id)
    if not state:
        state: dict = {
            "question": "",
            "history": [],
            "last_username": None
        }

    while True:
        question = input("\nAsk something (or 'exit'): ")

        if question.lower() == "exit":
            break
        
        state['question'] = question

        result = graph.invoke(state)

        print("\n--- RESPONSE ---:")
        print(result["response"])

        state = result

        memory.save(session_id, state)

if __name__ == "__main__":
    main()