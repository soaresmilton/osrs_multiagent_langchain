from app.agents.chat_agent.schema import ChatInput
from app.agents.chat_agent.agent import ChatAgent

def main():
    agent = ChatAgent()

    response = agent.run(
        ChatInput(question="How can I train combat efficiently?")
    )
    
    print(response)

if __name__ == "__main__":
    main()