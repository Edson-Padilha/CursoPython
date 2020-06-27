import matplotlib.pyplot as plt

def pesquisa(lista_cadastro, num, item):
    lista = []
arquivo = open('cadastro.txt','r')
lista_cadastro = []
for pessoa in lista_cadastro:
    if pessoa[num] == item:
        lista.append(pessoa)
return lista
x = [i for i in range(1,2)]
y = [i for i in range(11,12)]


     

plt.plot(x, y, Sexo, percentual, color = 'black') #Gráfico de linha
plt.bar(x, y, color = 'yellow') #Gráfico de barra
plt.title('Percentual por sexo')

plt.xlabel('Proporção')
plt.ylabel('Comparação')

plt.ylim(0, 500)#Limite de valor
plt.xlim(0, 7)

plt.show()