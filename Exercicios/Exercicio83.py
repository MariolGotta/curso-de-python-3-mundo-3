# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e
# fechados em ordem correta

expr = str(input('Digite a expressão: '))
pilha = []

for parent in expr:
    if parent == '(':
        pilha.append('(')
    elif parent == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
