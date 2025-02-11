# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

num = (int(input('Digite o primeiro número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))

print(f'Você digiou os valores {num}')

print(f'O número 9 apareceu {num.count(9)} vez(es)')

if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição pela primeira vez')
else:
    print('O número 3 não foi digitado nenhuma vez')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
