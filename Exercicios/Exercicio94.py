# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média

from operator import itemgetter

continuar = True

pessoa = dict()
dados = list()

somaidade = 0

while continuar == True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    dados.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N')
        continuar = str(input('Quer continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
    if continuar == 'S':
        continuar = True


print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')


media = somaidade/len(dados)
print(f'B) A média de idade é de {media:.2f} anos.')


print(f'C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) Lista de pessoas que estão acima da média: ')
if p in dados:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'    {k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
