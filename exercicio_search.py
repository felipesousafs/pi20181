import requests
import re
import requests_cache
import time
from bs4 import BeautifulSoup

start_time = time.time()

# requests_cache.install_cache('demo_cache')
# requests_cache.uninstall_cache()

occurrences = []

def search(keyword, url, depth):
    depth -= 1
    with requests_cache.disabled():
        response = requests.get(url)
    page = BeautifulSoup(response.content, 'html5lib')
    links = page.find_all('a')
    for link in links:
        if link.get('href') != None:
            # print('Find HTTP:', link.get('href').find('http'))
            if depth > 0 and link.get('href').find('http') > -1:
                print('Buscando na url: ', link.get('href'))
                search(keyword, link.get('href'), depth)
    print('Checando ocorrencias...')
    check_occurrence(response.text, keyword)

def check_occurrence(content, kw):
    indexes = [i.start() for i in re.finditer(kw.lower(), content.lower())]
    for index in indexes:
        occurrences.append(content[index-30:index+30])

def print_each_occurrence(occurrences):
    for occurrence in occurrences:
        print(occurrence)


# URLs e Keywords
url_ge = 'https://globoesporte.globo.com/'
keyword_ge = 'flamengo'
url_rege = 'http://regeneracao.pi.gov.br/'
keyword_rege = 'prefeitura'
url_americanas = 'https://www.americanas.com.br/'
keyword_americanas = 'geladeira'

depth = 2 # Em quantas camadas deve ser realizada a busca

# Chamada da função de busca
search(keyword_americanas, url_americanas, depth)

# Resultados
print('============ Ocorrências ============')
print_each_occurrence(occurrences)
print('------------------------------------')
print('Number of occurrences: ', occurrences.__len__())
print('Keyword: ', keyword_americanas)
print('URL: ', url_americanas)
print('Depth: ', depth)
print("--- Execution time: %s seconds ---" % (time.time() - start_time))