### Python Package Manager ###

#PIP Es un gestor para instalar modulos en python https://pypi.org

# pip --version
# pip list -> funciona para ver los modulos instalados

# numpy
# numpy da un extra para el manejo de operaciones, como conversión de listas a arreglos.
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)

#pandas

import pandas

# requests
#Sire para hacer peticiones a APIs

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(type(response.json()))
print(response.json())

pokemon_dict = response.json()

for pokemon in pokemon_dict:
    print(pokemon)
    
#Desarrollo de paquetes propios, un paquete es un conjunto de modulos
#__init__.py Guarda el contexto para que el paquete se comporte como un paquete.
# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1,4))