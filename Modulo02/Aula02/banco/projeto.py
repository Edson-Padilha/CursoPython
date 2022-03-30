# Implementar a construção de uma classe chamada conta - ok
# Deverão ter outras classes herdando desta - ContaCorrente | ContaPoupança | ContaSalario - ok
# Deverão existir métodos e atributos capazes de permitir
# Sacar, ver saldo, depositar e transferir valores para as contas quando fizer sentido!
# As classes conta, contaCorrente, contaPoupança e contaSalario ***Deverão ser arquivos separados
# Analisar e implementar os métodos e atributos utilizando conceito de herança a fim de evitar reescrever código
# Também deverá existir um arquivo chamado projeto onde terá um menu permitindo utilizar os respectivos 
# métodos e atributos.
# Nesse menu, deverá existir uma opção para selecionar o tipo de conta (corrente|poupança|salário)
# Apenas encerrar o projeto com a opção SAIR selecionada.
# Reescrever código.
# Validar o numero da conta com 5 digitos existente na lista.
# Tempo estimado: 40 min

from funcoes import validaTipoConta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from contaSalario import ContaSalario
import funcoes as f



contasC = [] # conta corrente
contasP = [] # conta poupanca
contasS = [] # conta salario

op = 0
tipoConta = 0

f.limpaTela()
while op != 4:
    print('Banco Proway\n'
            '1 - Criar Conta\n'
            '2 - Listar Conta\n'
            '3 - Excluir Conta\n'
            '4 - Sair\n')

    op = int(input('Informe a opção desejada: '))

    match op:
        case 1:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            numero = input('Informe o número da conta com 5 digítos: ')
            if len(numero) != 5:
                print('Numero inválido!')
                f.aguardaLimpa()
            
            else:
                match tipoConta:
                    case 1:
                        if numero in contasC:
                            print('Conta corrente já existente')
                        else:
                            contasC.append(numero)
                            print('Conta corrente cadastrada com sucesso...')
                        f.aguardaLimpa()

                    case 2:
                        if numero in contasS:
                            print('Conta salário já existente')
                            f.aguardaLimpa()

                        else:
                            contasS.append(numero)
                            print('Conta salário cadastrado com sucesso')
                            f.aguardaLimpa()

                    case outraOpcao:
                        if numero in contasP:
                            print('Conta poupança já existente')
                            f.aguardaLimpa()
                        else:
                            contasP.append(numero)
                            print('Conta poupança cadastrada com sucesso')
                            f.aguardaLimpa()
        case 2:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas corrente cadastradas' )
                    else:
                        print(contasC)
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas salários cadastradas')
                    else:
                        print(contasS)

                case outraCaso:
                    if len(contasP) == 0:
                        print('Não há contas poupança cadastradas')
                    else:
                        print(contasP)
            f.aguardaLimpa()
        case 3:
            tipoConta = f.validaTipoConta()
            f.limpaTela()
            match tipoConta:
                case 1:
                    if len(contasC) == 0:
                        print('Não há contas corrente cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            contasC.remove(numero)
                            print('Conta excluída com sucesso')
                case 2:
                    if len(contasS) == 0:
                        print('Não há contas cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            if not numero in contasS:
                                print('Conta inexistente')
                            else:
                                contasS.remove(numero)
                                print('Conta excluída com sucesso')
                case outraCaso:
                    if len(contasP == 0):
                        print('Não há contas poupança cadastradas')
                    else:
                        numero = input('Número da conta que deseja excluir: ')
                        if len(numero) != 5:
                            print('Número inválido')
                        else:
                            if not numero in contasP:
                                print('Conta inexistente')
                            else:
                                contasP.remove(numero)
                                print('Conta excluída com sucesso')
                    f.aguardaLimpa()
        case 4:
            print('Obrigado por usar o sistema')
            f.aguardaLimpa()
            break
        case outraCaso:
            print('Opção inválida')
            f.aguardaLimpa()
                    






