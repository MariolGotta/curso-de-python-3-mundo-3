# Faça um programa que tenha uma função chamada escreva(), que recebe um texto qualquer como parametro e mostre uma mensagem
# com tamanho adaptável
# Ex: escreva(Olá, Mundo!)
# Saída:
# ~~~~~~~~~~
# Olá Mundo!
# ~~~~~~~~~~


def texto(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt}')
    print('~'*tamanho)


texto('Olá Mundo!')
texto('Teste')
texto('Uma mensagem muito grande aqui')
