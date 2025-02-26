# Crie um programa onde o usuário possa digitar
# 7 valores numéricos e os cadastre-os em uma lista única
# que mantenha separados os valores pares e impares.]
# No final mostre os valores pares e ímpares em ordem crescente.

numero = list()
pares = list()
impares = list()

for c in range(0, 6):
    numero.append(int(input('Digite um número: ')))

    if numero[0] % 2 == 0:
        pares.append(numero[:])
    else:
        impares.append(numero[:])

    numero.clear()

    c += 1

print(pares)
print(impares)
