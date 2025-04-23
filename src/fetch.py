import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def fetch_page(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    response_content = response.content
    soup = BeautifulSoup(response_content, 'html.parser')
    return soup