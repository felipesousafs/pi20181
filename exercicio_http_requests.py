import requests

response = requests.get('http://libra.ifpi.edu.br/topo_ifpi.png')
print('Status code: ')
print(response.status_code)
print('Content Type: ')
print(response.headers['content-type'])
print('Content: ')
print(response.content)
file = open('img_ifpi_py.png', 'wb')
file.write(response.content)
file.close()