# Crie um programa que tenha uma funcao leiaint(), que vai funcionar em forma semelhante à funcao input() do python.
# Só que fazendo a validacao para aceitar apenas um valor numerico.
# Ex: n = leiaint('Digite um n')


def leiaInt(n):
    ok = False
    valor = 0
    print('-'*20)
    while True:
        n = str(input(n))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')
