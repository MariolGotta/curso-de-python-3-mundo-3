def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a+b
    print(f'A soma de A + B = {s}')


soma(3, 5)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador(2, 1, 4)
contador(8, 0)
contador(4, 4, 7, 6, 4, 5)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
