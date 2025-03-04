# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.


jogadores = list()


continuar = True

while continuar == True:

    perfil = dict()
    gols = list()

    perfil['nome'] = str(input('Nome do Jogador: '))
    jogos = int(input(f'Quantas partidas {perfil["nome"]} jogou? '))

    for c in range(0, jogos):

        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))

    perfil['gols'] = gols[:]
    perfil['total'] = sum(gols)
    jogadores.append(perfil.copy())

    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'S':
        continuar = True
    if continuar == 'N':
        break

print('-='*30)
print(f'{"cod":<4} {"nome":<12} {"gols":<15} {"total":<5}')
print('-'*40)
for i, jogador in enumerate(jogadores):
    print(
        f'{i:<4} {jogador["nome"]:<12}{str(jogador["gols"]):<20}{jogador["total"]:<5}')

print('-='*30)

continuar = True

while continuar == True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar): '))
    if busca < 0 or busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'    -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}: ')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    => No jogo {i+1}, fez {g} gols.')
        print('-'*40)

    if busca == 999:
        break


print('<<VOLTE SEMPRE>>')
