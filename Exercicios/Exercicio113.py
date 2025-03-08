# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(n=0):
    while True:
        try:
            n = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(
                '\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def leiaFloat(n=0):
    while True:
        try:
            n = float(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print(
                '\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
