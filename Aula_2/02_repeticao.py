idade = 151
lista_idades = [18,19,50,19,50,41,13,89,74]

print(idade)
# Imprimindo lista toda
print( lista_idades[2])
# Imprimindo item especifíco da lista

# Removendo um item da lista
# remove a primeira ocorrencia da lista
lista_idades.remove(19)
print(lista_idades)

# Removendo dado com a funcao pop
#
retorno_do_pop = lista_idades.pop(1)
print(lista_idades)
print(retorno_do_pop)

# Adicionando dados na lista com append
# adiciona o dado ao final da lista
lista_idades.append(54)
print(lista_idades)

# Mostrando o numero de instancias do dado na lista
print(lista_idades.count(18))

# Mostrando o numero total de dados da lista utilizando len
print(len (lista_idades))

# Fatiamento de lista 
# Imprimindo os 3 primeiros itens
print(lista_idades[:3])
# Imprimindo os 2 ultimos itens
print(lista_idades[ len(lista_idades)-3 : ])

index_penultimo_item = len(lista_idades)-3
print(lista_idades[ index_penultimo_item : ])

# Removendo todos os dados da lista
# lista_idades.clear()

print(lista_idades)
lista_idades.reverse()
print(lista_idades)

# Inserindo dados em uma posicao especifica da lista
lista_idades.insert(2,152)
print(lista_idades)

# Inserindo o numero 153 apos o 152
index = lista_idades.index(152)
lista_idades.insert(index + 1, 153)
print(lista_idades)

# Alterar dado em uma posicao especifica

lista_idades[0] = 150
lista_idades[4] = 154
print(lista_idades)

