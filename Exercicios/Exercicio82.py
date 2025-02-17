# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso crie duas listas extras qeu vão conter apenas os
# valores pares e os valores impares digitados respectivamente
# No final mostre o conteúdo das três listas geradas

lista1 = []
pares = []
impares = []

while True:
    valor = int(input('Digite um número: '))
    resp = str(input('Deseja continuar: [S/N] ')).upper()
    if valor % 2 == 0:
        lista1.append(valor)
        pares.append(valor)
    else:
        lista1.append(valor)
        impares.append(valor)
    if resp in 'N':
        break

print(lista1)

pares.sort()
print(pares)

impares.sort()
print(impares)
