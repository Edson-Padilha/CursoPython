lista = []
# Adicionando notas na lista
for i in range (4):
    nota = float(input(f'Digite nota {i+1}: '))
    lista.append(nota)

# Somando a lista
media = sum(lista) / len(lista)


if media >= 7:
    print('Aprovado')
elif media <= 5.5:
    print('Reprovado')
else:
    print('Recuperação')

   
# pass: deixa passar
# continue: volta para o inicio
# break: para, vai para o final