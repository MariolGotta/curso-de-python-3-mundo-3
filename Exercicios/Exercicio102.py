# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
# e o outro chamado show que será um valor lógico (opcinal) indicando se será ou não mostrado na tela o processo de calculo do fatorial


def fatorial(f, show=0):
    """Calcula o fatorial de um número

    Args:
        f (_type_): O número a ser calculado
        show (int, optional): Mostra ou não a conta. Defaults to 0.

    Returns:
        _type_: O valor do Fatorial de um número f
    """

    print('-'*20)
    c = 1
    for cont in range(f, 1, -1):
        f *= c
        c += 1
    if show == True:
        while c > 1:
            print(f'{c}', end=' x ')
            c -= 1
            if c == 1:
                return print(f'{c} = ', end=f'{f}')
    if show == False:
        return f'{f}'


fatorial(7, True)
help(fatorial)
