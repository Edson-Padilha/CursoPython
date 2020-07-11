from time import sleep

def linha(tam = 60):
    return '-' * tam

def cabecalho(texto):
    print(linha())
    print(texto.center(60))
    print(linha())

def menu(lista):
    cabecalho('\033[32m MENU PRINCIPAL\033[m')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m -> \033[34m{item}\033[m')
        cont += 1
    print(linha())
    opcao = leiaInt('\033[33m Digite sua opção:\033[m')
    return opcao

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Por favor, digite um numero válido.\033[m')
            continue
        else:
            return num

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        True 

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        #cabecalho('CLIENTES CADASTRADOS')
        #print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:8}{dado[2]:15}{dado[3]:4}{dado[4]:24}{dado[5]:10}{dado[6]:24}{dado[7]:20}{dado[8]:8}{dado[9]:30}'.upper())
    finally:
        a.close()

def cadastrar(arquivo, nome, nascimento, cpf, uf, cidade, cep, bairro, rua, numero, complemento):
    try:
        a = open(arquivo, 'at')
    except:
        print('ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{nasc};{cpf};{uf};{cidade};{cep};{bairro};{rua};{numero};{complemento}\n')
        except:
            print('ERRO na hora de escrever os dados')
        else:
            print(f'Cliente {nome}, cadastrado com sucesso!')
            a.close()

cabecalho('\033[1:32m SISTEMA CERVEJARIA JA TOM MEI \033[m')

menu(('Cadastrar Cliente\n','Cadastrar Produto\n','Listar Clientes\n','Listar Produtos\n','Sair\n'))

print(linha())

arquivo = 'teste.txt'

if not arquivoExiste(arquivo):
       criarArquivo(arquivo)
    #cabecalho('Arquivo encontrado com sucesso.')
#else:
    #cabecalho('Arquivo não encontrado!')

while True:
    resposta = menu(['Cadastrar Cliente','Listar Clientes','Cadastrar Produto','Listar Produtos','Sair'])
    if resposta == 1:
        cabecalho('Cadastrar Cliente')
        nome = str(input('Nome: '))
        nasc = str(input('Ano de nascimento: '))
        cpf = str(input('CPF: '))
        uf = str(input('Estado: '))
        cidade = str(input('Cidade: '))
        cep = str(input('Cep: '))
        bairro = str(input('Bairro: '))
        rua = str(input('Rua: '))
        numero = str(input('Numero: '))
        complemento = str(input('Complemento: '))
        cadastrar(arquivo, nome, nasc, cpf, uf, cidade, cep, bairro, rua, numero, complemento)
    elif resposta == 2:
        cabecalho('Listar Clientes')
        lerArquivo(arquivo)
    elif resposta == 3:
        cabecalho('Cadastrar Produto')
    elif resposta == 4:
        cabecalho('Listar Produtos')
    elif resposta == 5:
        cabecalho('Saindo do Sistema...')
        break
    else:
        cabecalho('\033[31m ERRO: Digite opção válida \033[m')
    sleep(2)

#arquivo = open ('C:\\Users\\Cliente\\Documents\\Python\\teste.text','a')
''' 
    clientes_cadastro = {'Nome':'','Nascimento':'', 'CPF':'', 'UF':'','Cidade':'','CEP':'','Bairro':'','Rua':'','Numero':'','Complemento':'' }'''
   