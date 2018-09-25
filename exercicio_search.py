import requests
from bs4 import BeautifulSoup

occurrences = []

def search(keyword, url, depth):
    depth -= 1
    response = requests.get(url)
    page = BeautifulSoup(response.content)
    links = page.find_all('a')
    for link in links:
        print('URL: ', link.get('href'))
        print('Depth: ', depth)
        print('Element <a>: ', link)
        if depth > 0 and link.get('href') != None:
            print('Find HTTP:', link.get('href').find('http'))
            if link.get('href').find('http') > -1:
                check_occurrence(response.text, keyword)
                search(keyword, link.get('href'), depth)

def check_occurrence(content, kw):
    number_of_ocurrences = content.count(kw)
    indexes = [i for i, x in enumerate(content) if x == kw]
    print('indexes: ', indexes)
    print('number of occurrences: ', number_of_ocurrences)
    print('=========== CONTENT ============== :', content)
url = 'https://globoesporte.globo.com/'
search('flamengo', url, 2)