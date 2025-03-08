from lib import cabecalho


def arquivoExiste(nome):
    import os
    os.chdir(
        r"C:\Users\Mario\OneDrive\Documentos\GitHub\curso-de-python-3-mundo-3\Exercicios\Ex115")
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    import os
    os.chdir(
        r"C:\Users\Mario\OneDrive\Documentos\GitHub\curso-de-python-3-mundo-3\Exercicios\Ex115")
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    import os
    os.chdir(
        r"C:\Users\Mario\OneDrive\Documentos\GitHub\curso-de-python-3-mundo-3\Exercicios\Ex115")
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o Arquivo!')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()
