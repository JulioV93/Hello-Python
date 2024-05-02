### Exception Handling ###

number_one, number_two = 5, 1
number_two = "1"

#try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una excepción
    print("Se ha ocurrido un error")

#try except else

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha ocurrido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

#try except else finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha ocurrido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")

#Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha ocurrido un ValueError")
except TypeError:
    print("Se ha ocurrido un TypeError")

#Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as e: #e es una variable que el nombre lo definde el programador
    #Concatenando el error capturado con un mensaje
    print("Ocurrio el siguiente error (1): " + str(e))
except Exception as error: 
    #Se ejecuta si no se produce una excepción
    print("Ocurrio el siguiente error (2): " + str(error))
    print(error)