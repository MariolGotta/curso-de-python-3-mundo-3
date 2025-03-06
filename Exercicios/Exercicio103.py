# Faça um programa que tenha uma funcao chamada ficha(), que receba dois parametros opicionais:
# o nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente


def ficha(nome='unknown', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato.')


gols = 0
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
