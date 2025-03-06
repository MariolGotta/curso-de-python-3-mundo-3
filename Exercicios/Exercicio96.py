# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (comprimento e largura) e mostre a área do terreno

def area(l, c):
    total = l*c
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {total:.1f}m³')


print(f'Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
