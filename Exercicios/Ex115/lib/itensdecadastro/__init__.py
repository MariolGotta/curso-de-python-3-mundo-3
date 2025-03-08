from lib import cabecalho


import os
from lib import cabecalho


def cadastrar(arq):
    os.chdir(
        r"C:\Users\Mario\OneDrive\Documentos\GitHub\curso-de-python-3-mundo-3\Exercicios\Ex115")

    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo!')
    else:
        escolha = 'S'  # Corrigindo a lógica do loop

        while escolha == 'S':
            nome = str(input('Nome: '))
            idade = cabecalho.leiaInt('Idade: ')

            try:
                a.write(f'{nome};{idade}\n')
            except:
                print('Houve um erro na hora de escrever os dados!')
            else:
                print(f'Novo registro de {nome} adicionado.')

            # Verificando se o usuário quer continuar
            escolha = input(
                'Deseja cadastrar outra pessoa? [S/N] ').upper()
            while escolha not in 'SN':
                print('Opção inválida, digite S ou N.')
                escolha = input('Digite [S/N]: ').upper()

        a.close()  # Fechando o arquivo apenas no final
