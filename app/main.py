from app.core.models.llm import get_llm


def main():
    llm = get_llm()
    response = llm.invoke("Hello, how are you?")
    print(response)

if __name__ == "__main__":
    main()