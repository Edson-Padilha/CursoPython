lista = [[], "oi", "thau",1.98,1, [1,2,3],{"agua":123},(), "fim"]

for i in lista:

    if type(i) == str:
        print('Tipo: 01 - String')
    elif type(i) == int:
        print('Tipo: 02 - Inteiro') 
    elif type(i) == float:
        print('Tipo: 03 - Real')
    elif type(i) == list:
        print('Tipo: 04 - Lista')
    elif type(i) == tuple:
        print('Tipo: 05 - Tupla')
    elif type(i) == dict:
        print('Tipo: 01 - Dicionário')

print(len(lista))
