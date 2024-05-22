### Type Hints ###

#A partir de la versión 3.6 de python se pueden tipar las variables, pero es un tipado debil, no se le puede obligar a python que tenga un tipo de dato.

#Sirve para un mejor entendimiento de lectura y programación. Mejora la intuición del editor de codigo al momento de tipar una variable.

#Es una buena practica tipar las variables, para una mejor interpretación del Backend y del programador.

#FastAPI utiliza este tipo de tipado para realizar validaciones del tipo de dato.

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))