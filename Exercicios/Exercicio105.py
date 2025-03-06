# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicionar também docstrings da função


def notas(*n, sit=0):
    """Função para analisar notas e situações de vários alunos.

    Args:
        n (int): uma ou mais notas de alunos.
        sit (True or False, optional): Indicando se deve ou não adicionar situação. Defaults to 0.

    Returns:
        Dict: dicionário com várias informações sobre a situação da turma
    """
    maior = menor = soma = 0
    turma = dict()
    for c, v in enumerate(n):

        if c == 0:
            maior = menor = v

        if v > maior:
            maior = v

        if v < menor:
            menor = v

        soma += v

    media = soma / len(n)

    turma['total'] = len(n)
    turma['maior'] = maior
    turma['menor'] = menor
    turma['media'] = media

    if sit == True:
        if media < 5:
            situação = 'RUIM'
        elif media >= 5 and media < 7:
            situação = 'RAZOÁVEL'
        else:
            situação = 'BOA'
        turma['situação'] = situação
    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
