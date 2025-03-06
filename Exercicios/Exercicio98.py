# Faça um programa que tenha uma função chamada contador(), que receba 3 parametros
# inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar tres contagens atraves da função criada:
# a) De 1 até 10 de 1 em 1
# b) De 10 até 0 de 2 em 2
# c) Uma contagem personalizada

from time import sleep


def contador(i, f, d):

    if d < 0:
        d *= -1

    if d == 0:
        d = 1

    print('-='*30)
    print(f'Contagem de {i} até {f} de {d} em {d}')
    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += d
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(f'{cont}', end=' ', flush=True)
            cont -= d
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
d = int(input('Passo: '))
contador(i, f, d)
