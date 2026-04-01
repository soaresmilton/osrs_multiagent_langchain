from app.graph.graph import build_graph

def main():
    graph = build_graph()

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

if __name__ == "__main__":
    main()