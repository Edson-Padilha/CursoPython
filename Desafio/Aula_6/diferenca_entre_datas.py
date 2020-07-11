from datetime import date, timedelta, relativedelta

dt = date.today() + timedelta(days =+ 120)# somente para dias
print(dt.strftime("%d/%m/%Y"))

dt = date.today() + relativedelta(weeks =+ 5)#somente para semanas
print(dt.strftime("%d/%m/%Y"))