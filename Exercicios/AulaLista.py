num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
# num.sort(reverse=True)
num.insert(2, 20)

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
num.pop(2)

print(num)
print(f'Essa lista tem {len(num)} elementos')


valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a[:]  # se for sem o [:] ele vincula as listas, se alterar em uma, altera na outra. Com o [:] ele cria uma cópia das listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')


gente = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in gente:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

totmai = totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
