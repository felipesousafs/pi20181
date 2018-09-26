import requests
import re
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
        if link.get('href') != None:
            print('Find HTTP:', link.get('href').find('http'))
            if depth > 0 and link.get('href').find('http') > -1:
                search(keyword, link.get('href'), depth)
    check_occurrence(response.text, keyword)

def check_occurrence(content, kw):
    number_of_ocurrences = content.lower().count(kw)
    indexes = [m.start() for m in re.finditer(kw.lower(), content.lower())]
    print('Indexes: ', indexes)
    print('kw: ', kw)
    print('number of occurrences: ', number_of_ocurrences)
    for index in indexes:
        print_each_occurrence(index, content.lower())
    # file = open('result.txt', 'w')
    # file.write(content.lower())
    # file.close()

def print_each_occurrence(index, content):
    print(index)
    print(content[100:200])
url = 'https://globoesporte.globo.com/'
search('flamengo', url, 1)