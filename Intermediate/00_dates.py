### Dates ###

#Las fechas no estan dentro del nucleo de Python, por lo que se debe utilizar un modulo desarrollado y que se instala por defecto.
from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    
    #Timestamp es la representación unica de un tiempo, formato POSIX
    timestamp = now.timestamp()

    print(timestamp)
    
now = datetime.now()

print_date(now)

year_2025 = datetime(2025, 1, 1, 15, 30, 50)

print_date(year_2025)

#time es un objetivo que se instancia vacio en primera instancia, sirve para llenarlo y manipularlo y trabajarlo de manera independiente.
from datetime import time

current_time = time()

print(current_time)

current_time = time(15,30,59)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#date es un objetivo que se instancia vacio en primera instancia, sirve para llenarlo y manipularlo y trabajarlo de manera independiente. Tiene una función en donde se puede obtener el día actual
from datetime import date

current_date = date.today()

print(current_date)

current_date = date(2024,5,5)

print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year, current_date.month+1,current_date.day)

print(current_date.month)

#Operaciones con fechas
diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

#Es una funcionalidad que nos permite trabajar con franjas de fechas, nos permite obtener la diferencia entre fechas-
from datetime import timedelta

start_timedelta = timedelta(200,100,100, weeks=10)
end_timedelta = timedelta(300,100,100, weeks=13)

print(start_timedelta - end_timedelta)
print(start_timedelta + end_timedelta)