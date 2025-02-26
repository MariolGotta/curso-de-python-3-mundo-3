# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

media = n = 0
boletim = list()
informacao = list()
notas = list()
continuar = True


while continuar == True:
    informacao.append(str(input('Nome: ')))
    informacao.append(int(input('Primeira Nota: ')))
    informacao.append(int(input('Segunda Nota: ')))
    media = (informacao[1]+informacao[2])/2
    boletim.append([n, informacao[0], media])
    notas.append([n, informacao[0], informacao[1], informacao[2]])

    informacao.clear()
    n += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'S':
        continuar = True
    if continuar == 'N':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for p in boletim:
    print(f'{p[0]:<4}{p[1]:<10}{p[2]:>8.1f}')


continuar = True
while continuar == True:
    print('-'*35)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if n == 999:
        print('Finalizando...')
        continuar = False

    if n <= len(notas)-1:
        print(f'Notas de {notas[n][1]} são [{notas[n][2]},{notas[n][3]}]')
print('<<<VOLTE SEMPRE>>>')
