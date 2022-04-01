import os
from time import sleep

def limpaTela():
    os.system('cls')

def aguarda():
    sleep(4)

def aguardaLimpa():
    aguarda()
    limpaTela()

def validaTipoConta():
    tipoConta = 0

    tipoConta = int(input('Informe o tipo de conta desejada\n'
            '\n1 - Conta corrente\n' +
            '2 - Conta salário\n'
            '3 - Conta poupança\n'
            '4 - Todas\n'))

    while (not tipoConta in [1,2,3,4]):
        print('Opção inválida!')
        aguardaLimpa()

        tipoConta = int(input('Informe o tipo de conta desejada\n'
                                '\n1 - Conta corrente\n' +
                                '2 - Conta salário\n'
                                '3 - Conta poupança\n'
                                '4 - Todas\n'))
        return tipoConta
def menuOperacoes(pTipoConta,valor = 0):# 1 corrente|2 salario|3 poupança
    aguardaLimpa()
    print('Operação desejada:\n ')
    match pTipoConta:
        case 1,3:
            while ( not opcao in [1,2,3,4,5]):
                print('Opção inválida!')
                opcao = int(input('1 - Sacar\n'
                                 ' 2 - Depositar\n'
                                  '3 - Transferir\n'
                                  '4 - Ver saldo\n'
                                  '5 - Voltar\n'))
                
                    
        case 2:
            while not (opcao in [1,2,3]):
                print('Opção inválida!')
                opcao = int(input('1 - Sacar\n' 
                                  '2  - Ver saldo\n'
                                  '3 - Voltar'))

               
            
        
        case outroCaso:
            return
            