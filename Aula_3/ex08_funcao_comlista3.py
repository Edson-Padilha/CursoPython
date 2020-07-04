notas = []

def media(lista):
    resultado = sum(lista)/len(lista)
    return resultado

for i in range (4):
    print('='*30)
    nota = float(input(f'Digite nota {i+1}: '))
    notas.append(nota)
<<<<<<< HEAD
print(media(notas))
=======
    
print('='*30)
print(f'Sua média é: {media(notas)}')
print('='*30)
>>>>>>> 0f3c047a4b8643234e5f2affdd54e50cefee694b
