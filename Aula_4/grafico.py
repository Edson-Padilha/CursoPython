import matplotlib.pyplot as plt

x = [i for i in range(1,7)]
y = [i for i in range(11,17)]

meses = ['Janeiro','Fevereiro','Março','Abril',
         'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

plt.plot(x, y, meses, valores, color = 'black') #Gráfico de linha
plt.bar(x, y, color = 'yellow') #Gráfico de barra
plt.scatter(x, y, color = 'red')#Gráfico de ponto
plt.title('Faturamento no primeiro semestre de 2017')

plt.xlabel('Solvente')
plt.ylabel('Produto resultante')

plt.ylim(0, 20)#Limite de valor
plt.xlim(0, 7)

plt.show()
