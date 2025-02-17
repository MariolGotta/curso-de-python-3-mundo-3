# Crie um programa onde o usuário passa a digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

digitados = []
continuar = True

while continuar == True:
    valor = (int(input('Digite um valor:')))

    if valor in digitados:
        print('Valor duplicado, não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        digitados.append(valor)

    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'S':
        continuar = True
    else:
        continuar = False

digitados.sort()
print(digitados)
