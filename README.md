**AWS Learning Chatbot**
A lightweight, terminal-based AI chatbot to help you learn AWS concepts — powered by Google Gemini and real-time DuckDuckGo search.

**Features:**
Ask anything related to AWS (e.g., What is EC2?)
Gets real-time answers using online sources
Uses Gemini AI API (free tier supported)
No OpenAI key needed
Fully terminal-based, no extra UI overhead

**Project Structure:**
learning-bot/
├── chatbot.py         # Main chatbot script
├── search.py          # DuckDuckGo search integration
├── .env               # Stores your Gemini API key
├── requirements.txt   # Python dependencies

**Setup Instructions:**
Clone the Repository

Create a Virtual Environment (Optional but Recommended):
"python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows"

Install Required Packages:
"pip install -r requirements.txt"

Add Your Gemini API Key:
"""Create a .env file in the root folder:"""
GEMINI_API_KEY=your_gemini_api_key_here

**Run the Chatbot:**
python chatbot.py

**How It Works**
Takes your input ➝ performs web search via DuckDuckGo HTML scraping
Feeds relevant context and question to Gemini API
Outputs a concise, informative response
Works entirely via terminal

**Notes**
You must have a working internet connection
Gemini free API has daily limits
Avoid spamming queries to stay within usage limits

**License**
MIT License
