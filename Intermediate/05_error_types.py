### Error Types ###

# SyntaxError
#print "¡Hola Comunidad!" # Descomentar para ver el Error
print("¡Hola Comunidad!")

# NameError
language = "Spanish" # Comentar para ver el Error
print(language)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
#print(my_list[5]) # Descomentar para ver el Error

# ModuleNotFoundError
#import maths # Descomentar para ver el Error
import math

# AttributeError
#print(math.PI) # Descomentar para ver el Error
print(math.pi)

# KeyError
my_dict = {"Nombre":"Julio", "Apellido":"Machado", "Edad":30}
#print(my_dict["nombre"]) # Descomentar para ver el Error
print(my_dict["Nombre"])

#TypeError
#print(my_list["0"]) # Descomentar para ver el Error
print(my_list[0])

# ImportError
#from math import PI # Descomentar para ver el Error
from math import pi

# ValueError
#my_int = int("10 Años") # Descomentar para ver el Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
#print(4/0) # Descomentar para ver el Error
print(4/2)