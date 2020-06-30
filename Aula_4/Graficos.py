  
import matplotlib.pyplot as plt #Biblioteca para gráfico

x = [i for i in range (1,7)]
y = [i for i in range (11,17)]
meses = ['Janeiro','Fevereiro','Março','Abril','maio','junho']
valores = [85135, 107697, 110256, 129236, 138859, 109986]

#plt.plot(x, y) # gráfico linha
plt.bar(meses, valores, color = 'yellow') # gráfico de barra
#plt.scatter(x, y) # gráfico de pontos
plt.title ('Faturamento Semestral')
plt.xlabel ('Meses')
plt.ylabel ('Valor Faturado R$')

plt.show()