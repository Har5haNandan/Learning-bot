import requests
from bs4 import BeautifulSoup

def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num=5"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Search error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3')
        link = g.find('a')
        if title and link:
            results.append({
                'title': title.text,
                'link': link['href']
            })

    return results
