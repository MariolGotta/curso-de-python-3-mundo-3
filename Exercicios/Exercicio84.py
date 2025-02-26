# Faça um programa que leia nome e peso de várias
# pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves

maiorpeso = menorpeso = c = 0

informacao = list()
dados = list()
continuar = True

while continuar == True:
    informacao.append(str(input('Nome: ')))
    informacao.append(float(input('Peso: ')))
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()

    if c == 0:
        menorpeso = maiorpeso = informacao[1]
    else:
        if informacao[1] > maiorpeso:
            maiorpeso = informacao[1]
        if informacao[1] < menorpeso:
            menorpeso = informacao[1]

    dados.append(informacao[:])
    informacao.clear()
    c += 1

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    if continuar == 'S':
        continuar = True
    elif continuar == 'N':
        break
print(f'Ao todo, você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maiorpeso:.1f}kg. Peso de ', end='')
for p in dados:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorpeso:.1f}kg. Peso de ', end='')
for p in dados:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
