# Crie um programa que vai ler vários números e colocar em uma lista
# Depois disso mostre:
# Quantos números foram digitados
# Lista de valores ordenada em forma decrescente
# Se o valor 5 foi digitado e está ou não na lista

n = []
continuar = True

while continuar == True:
    valor = int(input('Digite um valor: '))
    n.append(valor)

    resp = str(input('Deseja continuar? [S/N] ')).upper()

    if resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'S':
        continuar = True
    else:
        continuar = False

n.sort(reverse=True)

print('-='*30)
print(f'Você digitou {len(n)} elementos')
print(f'Os valores em ordem decrescente são {n}')

if 5 in n:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não faz parte da lista')
