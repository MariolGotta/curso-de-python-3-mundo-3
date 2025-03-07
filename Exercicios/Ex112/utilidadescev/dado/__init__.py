def leiadinheiro(valor):
    v1 = str(input(f'{valor}')).replace(',', '.').strip()
    while v1.isalpha() == True or v1 == '':
        print(f'\033[1;31mERRO: "{v1}" é um preço inválido\033[0m')
        v1 = str(input(f'{valor}')).replace(',', '.').strip()

    vf = float(v1)

    return vf


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
