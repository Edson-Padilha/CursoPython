# Tuplas
lista = [10,12]

tupla = (10,12,15,89,44,55)
print(tupla[1])
print(tupla[1:3])

print(tupla)

# Código abaixo gera exceção pois a tupla não permite alterações
#tupla[1] = 88

print(tupla)
lista_notas = [10,8, 6, 4]
# Criando uma tupla com tipos de dados diferentes, incluindo lista
tupla_aluno = ('Edson', 'Maykon', 15, [10,8,6,4])
# Criando uma tupla com tiposde dados diferentes, incluindo  lista
tupla_aluno[3][2] = 8
print(tupla_aluno)

# Convertendo tupla em lista
lista_aluno = list(tupla_aluno)
print(lista_aluno)

# Dicionários
aluno = {'nome' : 'maykon','sobrenome':'granemann','idade':18}
aluno2 = {'nome' : 'Edson','sobrenome':'Padilha','idade': 38}


print(aluno)
lista = [aluno,aluno2]
print(aluno)
print(aluno['nome'])
aluno['nome'] = Tadeu

#dict_numeros = {'n':}
# Imprimindo dicionários utilizando for
for a in lista:
    # Imprimindo cada dado do dicionário através das chaves
    print(a['nome'])
    print(a['sobrenome'])
    print(a['idade'])
    print(a['lista_notas'])

lista_alunos = []
for i in range (2):
    dict_aluno = {}
    dict_aluno['nome'] = input('Digite o nome: ')
    dict_aluno['sobrenome'] = input('Digite sobrenome: ')
    dict_aluno['idade'] = input('Digite idade: ')
    lista_alunos.append(dict_aluno)

for a in lista_aluno:
    print('Usuario cadastrado: ', a['sobrenome'], a['idade'])