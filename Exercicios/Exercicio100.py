# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
# de todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        num = randint(0, 10)
        print(f'{num}', end=' ', flush=True)
        lista.append(num)
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    pares = list()
    soma = 0
    for v in lista:
        if v % 2 == 0:
            pares.append(v)
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
