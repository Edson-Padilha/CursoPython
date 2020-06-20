print('='*30)

nota = float(input('Digite uma nota: '))
print('Digite 0 para sair')
#while nota != 0:

if nota <= 5.50:
    print('Reprovado')
elif nota >= 7:
    print('Aprovado')
else:
    print('Recuperação')
