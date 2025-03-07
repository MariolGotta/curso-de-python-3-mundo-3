

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
    """Calcula o aumento de um determinado preço, retornando o resultado com
    ou sem formatação.

    Args:
        n (int, optional): o preço que se quer reajustar. Defaults to 0.
        q (int, optional): a porcentagem de aumento. Defaults to 0.
        format (bool, optional): o valor reajustado com ou sem formato. Defaults to False.

    Returns:
        _type_: _description_
    """
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


def resumo(p, aumento=10, diminuição=5):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p):>8}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(p, aumento, True)}')
    print(f'{diminuição}% de redução: \t{diminuir(p, diminuição, True)}')
    print('-'*30)
