import requests
from bs4 import BeautifulSoup

def search(keyword, url, depth):
    response = requests.get(url)
    page = BeautifulSoup(response.content)
    links = page.find_all('a')
    for link in links:
        print('Link: ', link.get('href'))
        print('Depth: ', depth)
        if depth > 0:
            search(keyword, link.get('href'), depth)

url = 'http://libra.ifpi.edu.br'
search('ifpi', url, 0)