arquivo = open('cadastro.txt','r')
lista_cadastro = []

for pessoa in arquivo:
    pessoa = pessoa.strip()#Comando para separar
    pessoa = pessoa.split(';')
    lista_cadastro.append(pessoa)
   
arquivo.close()

mulher = []

for pessoa in lista_cadastro:
    if pessoa[3] == 'f':
        mulher.append(pessoa)

    arquivo = open('cadastro.txt','W')

for pessoa in mulher:
    pessoa_str = ';'.join(pessoa)+'\n'
    arquivo.write