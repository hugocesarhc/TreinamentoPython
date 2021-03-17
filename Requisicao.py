'''
requisições WEB é importante usar as várias bibliotecas python que existem

'''

import requests

try:
    requisicao = requests.get('http://g1.com.br')
    print(requisicao.text)
except Exception as e:
    print("requisição deu erro", e)
