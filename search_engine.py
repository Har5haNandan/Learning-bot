from googlesearch import search
import requests
from bs4 import BeautifulSoup

def scrape_snippet(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(page.text, "html.parser")
        for p in soup.find_all("p"):
            text = p.get_text().strip()
            if len(text) > 80:
                return text
    except:
        return "Snippet not available"
    return "No content found"

def search_google(query, count=3):
    try:
        urls = list(search(query, num_results=count))
        results = []
        for url in urls:
            snippet = scrape_snippet(url)
            results.append({
                "title": url.split('/')[2],
                "snippet": snippet,
                "url": url
            })
        return results
    except Exception as e:
        print(f"[Search Error] {e}")
        return []
