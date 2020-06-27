arquivo = open('cadastro.txt','r')
lista_cadastro = []

for pessoa in arquivo:
    pessoa = pessoa.strip()#Comando para separar
    pessoa = pessoa.split(';')
    lista_cadastro.append(pessoa)
   

arquivo.close()

['300', 'LiÃ©ge', '27', 'f', 'aline.moretti.sanches@gmail.com', '022916682770']


for pessoa in lista_cadastro:
    if pessoa[0] == '300': #Pode ser usado int(pessoa[0]) == 300:
        print(pessoa)
        break
    if pessoa[3].upper() == 'F':#Procura por coluna lista
        print(pessoa)
    if '1' in pessoa[0] or 'A' in pessoa[1]:
        print(pessoa)
    
    #print(i)

#print(lista_cadastro)

