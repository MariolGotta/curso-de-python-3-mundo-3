# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
# O sistema só irá ter 2 opções, cadastrar uma pessoa nova e listar todas as pessoas cadastradas.

from lib import itensdecadastro, cabecalho, arquivo
from time import sleep

arq = 'nomes.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    try:
        cabecalho.format('MENU PRINCIPAL')
        opcoes = (['Ver pessoas cadastradas',
                  'Cadastrar novas pessoas',
                   'Sair do sistema']
                  )
        escolha = cabecalho.menu(opcoes)
        if escolha == 1:
            cabecalho.format('PESSOAS CADASTRADAS')
            arquivo.lerArquivo(arq)
            sleep(2)
            continue
        elif escolha == 2:
            cabecalho.format('NOVO CADASTRO')
            itensdecadastro.cadastrar(arq)
            continue
        elif escolha == 3:
            cabecalho.format(f'SAINDO DO SISTEMA... ATÉ LOGO!')
            break
        else:
            print(
                '\033[31mOpção não encontrada! Digite uma opção que está na lista.\033[m')
            sleep(1)

    except (ValueError):
        print('Digite um número válido!')
        continue
