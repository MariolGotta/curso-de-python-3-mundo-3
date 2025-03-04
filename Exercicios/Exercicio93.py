# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feito durante o campeonato.

perfil = dict()
gols = list()

partidas = 0

perfil['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {perfil['nome']} jogou? '))

for c in range(0, jogos):

    gols.append(int(input(f'   Quantos gols na partida {c}? ')))
    partidas += 1

perfil['gols'] = gols[:]
perfil['total'] = sum(gols)
print('-='*30)

print(perfil)

print('-='*30)

for c, v in perfil.items():
    print(f'O campo {c} tem o valor {v}')

print('-='*30)

print(f'O jogador {perfil['nome']} jogou {len(perfil["gols"])} partidas')


for i, v in enumerate(perfil['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')

print(f'Foi um total de {perfil['total']} gols')
