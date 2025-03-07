def metade(n=0):
    met = n / 2
    return met


def dobro(n=0):
    dob = n*2
    return dob


def aumentar(n=0, q=0):
    total = n*(1+q/100)
    return total


def diminuir(n=0, q=0):
    total = n*(1-q/100)
    return total


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
