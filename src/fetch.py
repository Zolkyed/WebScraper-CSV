import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    response_content = response.content
    soup = BeautifulSoup(response_content, 'html.parser')
    return soup