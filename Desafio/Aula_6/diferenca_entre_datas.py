from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from time import sleep, time

dt = date.today() + timedelta(days =+ 120)# somente para dias
print(dt.strftime("%d/%m/%Y"))

dt = date.today() + relativedelta(weeks =+ 5)#somente para semanas
print(dt.strftime("%d/%m/%Y"))

#Bastante usado para envio em massa de email e mensagem de whats sem levantar suspeita
while True:
    print('Despertador')
    sleep(5)
    break

#Quando precisa cronometrar tempo, ex: quanto demora para enviar 1 email ou 
a = time()
print('Olá')
print(time() - a)