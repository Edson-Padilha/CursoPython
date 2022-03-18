import estoque
op =0
def menu():
    print('ESCOLHA UMA OPÇÃO'.center(40,'-'))
    print('|'+(' 1 - Cadastrar Item'.ljust(38,' ')+('|')))
    print('|'+(' 2 - Excluir Item'.ljust(38,' ')+('|')))
    print('|'+(' 3 - Atualizar Item'.ljust(38,' ')+('|')))
    print('|'+(' 4 - Visualizar Item'.ljust(38,' ')+('|')))
    print('-'.ljust(40,'-'))


def opcao(x):
    match x:
        case 1:
            item = input('Digite o nome do produto: ').upper()
            estoque.cadastrar(item)
            print(estoque.produtos)
        

menu()
opcao(1)