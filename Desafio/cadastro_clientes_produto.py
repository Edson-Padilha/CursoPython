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
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
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

cabecalho('\033[1:32m SISTEMA CERVEJARIA JA TOM MEI \033[m')

menu(('Cadastrar Cliente\n','Cadastrar Produto\n','Listar Clientes\n','Listar Produtos\n',' Sair\n'))

print(linha())

#while True:
    #resposta = (['Cadastrar Cliente','Ver Clientes','Cadastrar Produto','Ver Produtos','Sair'])

arquivo = open ('C:\\codepython\\CursoPython\\Desafio\\teste.text','a')
clientes = []
for i in range(1,3):
   
    clientes_cadastro = {'Id':'','Nome':'','Nascimento':'', 'CPF':'', 'UF':'','Cidade':'','CEP':'','Bairro':'','Rua':'','Numero':'','Complemento':'' }
    #clientes_cadastro['Id'] = clientes.index()
    clientes_cadastro['Nome'] = input('Digite o nome completo: \n' ).upper()
    #clientes_cadastro['Nascimento'] = input('Digite data de nascimento: \n')
    #clientes_cadastro['CPF'] = input('Digite o cpf: \n' )
    #clientes_cadastro['UF'] = input('Estado: ').lower()
    #clientes_cadastro['Cidade'] = input('Cidade: ').lower()
    #clientes_cadastro['CEP'] = input('Cep: ' )
    #clientes_cadastro['Bairro'] = input('Bairro: ').lower()
    #clientes_cadastro['Rua'] = input('Endereço: ').lower()
    #clientes_cadastro['Numero'] = input('Numero: ')
   # clientes_cadastro['Complemento'] = input('Complemento: ').lower()
    clientes.append(clientes_cadastro)
    
    arquivo.writelines(clientes_cadastro)
print(clientes)
