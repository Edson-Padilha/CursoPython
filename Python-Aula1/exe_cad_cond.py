print('\n')
print('='*15, 'Sistema de bebidas', '='*15)
print('\n')
nome = input('Nome de usuário: ')
idade = int(input('Digite sua idade: '))

if idade >= 18:
    bebida = input('Digite a bebida: ')
    print(nome,', comprou ', bebida)
else:
    print('VENDA NÃO PERMITIDA PARA MENORES DE 18 anos,', nome)
print('\n')
print('='*15, 'Fim do Programa', '='*15)
print('\n')