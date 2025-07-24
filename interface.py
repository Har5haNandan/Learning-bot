from chatbot import get_answer

def run_cli():
    print("AWS Learning Chatbot | Type 'exit' to quit.\n")
    while True:
        query = input("🧑 You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response, sources = get_answer(query)
        print("\n🤖 Bot:", response)
        print("\n🔗 Sources:")
        for src in sources:
            print(f" - {src['title']}: {src['url']}")
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    run_cli()
