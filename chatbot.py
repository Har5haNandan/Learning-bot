import openai
from config import OPENAI_API_KEY, OPENAI_MODEL
from search_engine import search_google
from context_manager import ChatContext

openai.api_key = OPENAI_API_KEY
context = ChatContext()

def generate_prompt(query, sources):
    search_summary = "\n".join([f"- {item['snippet']} (Source: {item['url']})" for item in sources])
    prompt = (
        f"{context.get_prompt()}"
        f"User asked: {query}\n\n"
        f"Here are some web results:\n{search_summary}\n\n"
        f"Using the above, provide a helpful and clear response:"
    )
    return prompt

def ask_chatgpt(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return completion.choices[0].message["content"]
    except Exception as e:
        print(f"[ChatGPT Error] {e}")
        return "Sorry, something went wrong while generating the response."

def get_answer(query):
    sources = search_google(query)
    prompt = generate_prompt(query, sources)
    response = ask_chatgpt(prompt)
    context.add(query, response)
    return response, sources

if __name__ == "__main__":
    run_chatbot()
