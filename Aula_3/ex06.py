# Crie um programa que leia um número de 1 a 100.
# Faça uma busca sequencial na tupla e mostre a posição 
# que se encontra o número

# Use o for e o break

num = int(input('Digite numero: '))
cont = 0
tupla = (98, 93, 71, 78, 4, 12, 47, 50, 21, 39, 33, 
         38, 23, 9, 28, 96, 24, 86, 26, 31, 73, 16, 
         13, 87, 44, 89, 69, 53, 94, 40, 67, 37, 55, 
         62, 91, 57, 36, 72, 79, 61, 83, 48, 56, 64, 
         17, 65, 88, 20, 27, 84)

for i in tupla:
    
    if i == num:
       print(cont)
       break
    cont += 1

