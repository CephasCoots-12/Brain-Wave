import requests
from bs4 import BeautifulSoup

def get_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for item in soup.find_all("a", class_="storylink")[:10]:
        headlines.append(item.text)
    return headlines

news = get_news()
