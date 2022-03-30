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
            '1 - Conta corrente\n'
            '2 - Conta salário\n'
            '3 - Conta poupança\n'))

    while (not tipoConta in [1,2,3]):
        print('Opção inválida!')
        aguardaLimpa()

        tipoConta = int(input('Informe o tipo de conta desejada\n'
                                '1 - Conta corrente\n'
                                '2 - Conta salário\n'
                                '3 - Conta poupança\n'))
        return tipoConta
