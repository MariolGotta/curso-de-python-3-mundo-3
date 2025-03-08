# Crie um código em python que teste se o site Pudim está acessível pelo computador usado do usuário.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('Consegui acessar o site!')
    print(site.read())
