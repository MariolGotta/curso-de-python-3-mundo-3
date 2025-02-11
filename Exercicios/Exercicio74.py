# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla

from random import randint

n = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
for c in n:
    print(f'{c} ', end=' ')
print(f'\nO menor valor é: {max(n)}')
print(f'O maior valor é: {min(n)}')
