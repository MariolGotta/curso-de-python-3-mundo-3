def soma(a=0, b=0, c=0):
    """Faz a soma de tres valores e mostra o resultado na tela.

    Args:
        a (int, optional): O primeiro valor. Defaults to 0.
        b (int, optional): O segundo valor. Defaults to 0.
        c (int, optional): O terceiro valor. Defaults to 0.
    Função criada por Mario Lucio
    """

    s = a+b+c
    print(f'A soma vale {s}')


help(soma)
soma(5, 2)
soma(2, 9, 4)


def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')


def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


def soma(a=0, b=0, c=0):

    s = a+b+c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É Par')
else:
    print('É Ímpar')
