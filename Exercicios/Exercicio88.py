# Faça um programa que ajude um jogador da Mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo cadastrado tudo em uma lista composta.
from random import randint
from time import sleep

numeros = list()
jogos = list()

print('-'*30)
print(' '*5 + 'JOGO NA MESA SENA' + ' '*5)
print('-'*30)

qtdade = int(input('Quantos jogos você deseja fazer? '))
print('-='*5 + f'SORTEANDO {qtdade} JOGOS' + '-='*5)
for c in range(0, qtdade):
    for a in range(0, 6):
        num = randint(1, 60)
        if num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

    c += 1

for v in range(0, qtdade):
    sleep(0.5)
    print(f'Jogo {v+1}: {jogos[v]}')
    v += 1

print('-='*5 + f'< BOA SORTE! >' + '-='*5)
