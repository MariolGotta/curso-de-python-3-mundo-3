# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por
# extenso de 0 até 20. Seu programa deverá ler um numero pelo teclado entre 0 e 20
# e mostralo por extenso

n = int(input('Digite um número entre 0 e 20: '))

while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))


extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize',
           'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

print(f'Você digiou o número {extenso[n]}')
