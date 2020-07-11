divisao = lambda var , var1 : var / var1
print(divisao(12,3))

multiplicacao = lambda var, var1 : var * var1
print(multiplicacao(9,3))

def cadastro (nome, idade, sexo="N/D"):
    print(f'Seu nome é {nome}, você tem {idade} anos e é do sexo {sexo}')

cadastro("Luiza", 18)

lista = ['Edson', 'm', '23']
cadastro(*lista)#Chama todos os elementos da lista


#dic = {'nome: ''','idade:''','sexo: '''}
#cadastro(**lista)

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list(map(lambda x : x*3, lista))#multiplica 
print(resultado)

tempo = [i for i in range (25)]

montante = lambda t, valor = 200, i = 10: valor*(1+(i/100))**t
resultado = list(map(montante, tempo))
print(tempo)
print(resultado)

lista = ['m','f','f','m','m']
filtro = lambda sexo: True if sexo == 'm' else False
resultado = list(filter(filtro, lista))#Utilizando a função filtro

print(lista)
print(resultado)

lista = [i for i in range(31)]
filtro = lambda multiplos: True if (multiplos%3) == 0 else False# Filtro com multiplos de 3
resultado = list (filter(filtro, lista))

print(lista)
print(resultado)

from random import randint
lista = [randint(1,61) for i in range(6)]
print(lista)

from functools import reduce

lista = [ i for i in range (10)]
funcao = lambda x,y : x + y
print(lista)
print(reduce(funcao, lista))# soma todos os elementos da lista

from functools import reduce

lista = [ i for i in range (1,10)]
funcao = lambda x,y : x * y
print(lista)
print(reduce(funcao, lista))# Multiplica todos os elementos da lista

from functools import reduce

lista = [1,1,2,2,3,3,4,4,4,10,10]
funcao = lambda x,y : x ^ y
print(reduce(funcao, lista))
