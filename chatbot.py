import os
from dotenv import load_dotenv
from search import google_search
import google.generativeai as genai

# Load .env variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model name (must include full path for v1beta)
MODEL_NAME = "gemini-1.5-flash"

def get_answer_from_gemini(question, web_results):
    try:
        context_text = "\n".join([f"{i+1}. {r}" for i, r in enumerate(web_results)]) or "No context found."
        prompt = f"""Answer the following question using the context below:
        ---
        Question: {question}
        ---
        Context:
        {context_text}
        ---
        Provide a clear, helpful answer for someone learning AWS."""

        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API error: {str(e)}"

def main():
    print("🧠 AWS Learning Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        print("\n🔎 Searching online...")
        search_results = google_search(user_input)

        print("\n💬 Generating answer...\n")
        answer = get_answer_from_gemini(user_input, search_results)

        print("🤖 Bot:")
        print(answer)

        print("\n🔎 Sources:")
        if search_results:
            for result in search_results:
                print(f"- {result}")
        else:
            print("- No search results found.")
        print("\n---\n")

if __name__ == "__main__":
    main()

