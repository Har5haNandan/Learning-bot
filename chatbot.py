import os
from openai import OpenAI
from dotenv import load_dotenv
from search import google_search 
import time

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Conversation history
conversation_history = []

def get_chatgpt_response(user_query, context=[]):
    try:
        messages = [{"role": "system", "content": "You are a helpful and accurate AI assistant that helps people learn AWS with real-time information and citations."}]
        for entry in context:
            messages.append({"role": "user", "content": entry["user"]})
            messages.append({"role": "assistant", "content": entry["bot"]})
        messages.append({"role": "user", "content": user_query})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"ChatGPT API error: {e}"

def format_sources(results):
    if not results:
        return "- No search results found."
    return "\n".join([f"- {res['title']}: {res['link']}" for res in results[:3]])

def chatbot():
    print("AWS Learning Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("\n🔎 Searching online...\n")
        search_results = google_search(user_input)
        sources = format_sources(search_results)

        print("💬 Generating answer...\n")
        time.sleep(1)  # Simulate thinking

        # Add sources to user query as context
        search_context = "\n\nSources:\n" + "\n".join([res['link'] for res in search_results[:3]])
        full_prompt = f"{user_input}\n\nUse these sources to help:\n{search_context}"

        bot_reply = get_chatgpt_response(full_prompt, conversation_history)

        conversation_history.append({
            "user": user_input,
            "bot": bot_reply
        })

        print(f"🤖 Bot:\n{bot_reply}\n")
        print(f"🔎 Sources:\n{sources}\n")
        print("---\n")

if __name__ == "__main__":
    chatbot()
