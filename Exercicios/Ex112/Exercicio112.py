# Dentro do pacote utilidadescev que criamos no desafio 111, temos
# um módulo chamado dado. Crie uma função chamada leiadinheiro() que seja capaz de funcionar
# como uma função input(), mas como uma validação de dados para aceitar apenas valores que sejam monetários.


from utilidadescev import moeda, dado


p = dado.leiadinheiro('Digite o preço R$: ')
moeda.resumo(p, 35, 22)
