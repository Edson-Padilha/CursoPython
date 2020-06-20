def soma(num, num1):
    soma_funcao = num + num1
    return soma_funcao

def subtrair(num, num1):
    subtrair_funcao = num - num1
    return subtrair_funcao

def divisao(num, num1):
    divisao_funcao = num / num1
    return divisao_funcao

def multiplicar(num, num1):
    multiplicar_funcao = num * num1
    return multiplicar_funcao

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
        resultado = divisao(num, num1)
        print(resultado)
    if opcao == '2':
        resultado = multiplicar(num, num1)
        print(resultado)
    if opcao == '3':
        resultado = soma(num, num1)
        print(resultado)
    if opcao == '4':
        resultado = subtrair(num, num1)
        print(resultado)
  

  
    