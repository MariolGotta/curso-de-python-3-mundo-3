def metade(n=0, format=False):
    met = n / 2
    if format == True:
        return moeda(met)
    else:
        return met


def dobro(n=0, format=False):
    dob = n*2
    if format == True:
        return moeda(dob)
    else:
        return dob


def aumentar(n=0, q=0, format=False):
    total = n*(1+q/100)
    if format == True:
        return moeda(total)
    else:
        return total


def diminuir(n=0, q=0, format=False):
    total = n*(1-q/100)
    if format == True:
        return moeda(total)
    else:
        return total


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
