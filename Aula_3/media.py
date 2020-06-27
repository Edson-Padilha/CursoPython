

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))
   
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print('Aprovado')
elif media <= 5.5:
    print('Reprovado')
else:
    print('Recuperação')
