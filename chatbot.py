import os
import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def search_google(query):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(
            f"https://www.google.com/search?q={query}",
            headers=headers,
            timeout=5
        )

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for g in soup.find_all('div', class_='tF2Cxc')[:3]:  # Top 3 results
            title_tag = g.find('h3')
            link_tag = g.find('a')
            if title_tag and link_tag:
                title = title_tag.get_text()
                link = link_tag['href']
                results.append(f"{title}: {link}")

        return results if results else ["No search results found."]
    except Exception as e:
        return [f"Error while searching: {str(e)}"]

def ask_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"ChatGPT API error: {str(e)}"

def run_chatbot():
    print("🧠 AWS Learning Chatbot (with Google Search)")
    print("Type 'exit' to quit.\n")

    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        # Step 1: Search Google
        search_results = search_google(user_input)
        search_summary = "\n".join(search_results)

        # Step 2: Send both user input + search to ChatGPT
        prompt = (
            f"The user asked: '{user_input}'\n\n"
            f"Here are some search results from Google:\n{search_summary}\n\n"
            "Now provide a helpful and clear response tailored for AWS learners."
        )

        response = ask_chatgpt(prompt)

        # Save to history
        chat_history.append({"user": user_input, "bot": response})

        # Print response
        print(f"\n🤖 Bot:\n{response}\n")
        print("🔎 Sources:")
        for res in search_results:
            print(" -", res)
        print("\n---\n")

if __name__ == "__main__":
    run_chatbot()
