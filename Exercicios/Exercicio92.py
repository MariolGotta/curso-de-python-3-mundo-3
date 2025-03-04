# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário. Se for o caso a CTPS for diferente de 0, o dicionario receberá também o ano
# de contratação e o salário. Calcule e acrescente além da idaide, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
dados['idade'] = idade
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salário: R$'))
    aposentadoria = idade + \
        ((35 + dados['contratacao']) - date.today().year)
    dados['aposentadoria'] = aposentadoria

print('-='*30)
for c, v in dados.items():
    print(f' - {c} tem o valor {v}')

print(dados)
