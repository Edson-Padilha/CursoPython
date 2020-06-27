notas = []

def media(lista):
    resultado = sum(lista)/len(lista)
    return resultado

for i in range (4):
    nota = float(input(f'Digite nota {i+1}: '))
    notas.append(nota)
print(media(notas))
