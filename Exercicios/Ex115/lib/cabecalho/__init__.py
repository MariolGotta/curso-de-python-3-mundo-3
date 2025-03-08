def format(texto):
    print('-'*42)
    print(texto.center(42))
    print('-'*42)


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


def menu(opcoes):
    c = 1
    for i in opcoes:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print('-'*42)
    escolha = leiaInt('\033[32mSua Opção: \033[m')
    return escolha
