# Crie um pacote chamado utilidadescev que tenha dois módulos internos
# chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107,108,109
# para o primeiro pacote e mantenha tudo funcionando.


from utilidadescev import moeda


p = float(input('Digite o preço R$: '))
moeda.resumo(p)
