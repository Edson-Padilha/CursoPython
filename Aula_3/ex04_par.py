num = int(input('Digite numero: '))

cont = 2
while cont <= num:
    cont = cont + 1    
    if (cont % 2) == 0:
        continue
    print(cont)
