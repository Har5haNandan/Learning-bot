
import requests
from bs4 import BeautifulSoup

def google_search(query, max_results=3):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://html.duckduckgo.com/html/?q={query}"
    results = []

    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.find_all("a", {"class": "result__a"}, limit=max_results)

        for link in links:
            href = link.get("href")
            if href:
                results.append(href)
    except Exception as e:
        results.append(f"Search error: {str(e)}")

    return results

