
menu = '''
Opções:
1 para divisão
2 para multiplicar
3 para somar
4 para diminuir
S para sair'''

while True:
    opcao = input('Qual sua opção: ')
    num = int(input('Digite numero: '))
    num1 = int(input('Segundo numero: '))

if opcao == '1':
    resultado = num / num1
    print(f'Resultado: {resultado}')
if opcao == '2':
    resultado = num * num1
    print(f'Resultado: {resultado}')
if opcao == '3':
    resultado = num + num1
    print(f'Resultado: {resultado}')
if opcao == '4':
    resultado = num - num1
if opcao == 'S'.isupper:    
    print(f'Saindo do Programa!')
    break
    