### Modules ###

#El archivo 10_functions tira error por la nomenclatura del nombre dle fichero, por lo que se copio y creo uno nuevo.

#Manera de llamar otros ficheros o modulos.
import my_module

my_module.sumValue(1,2,3)
my_module.printValue("Hola Python")

#manera de llamar una unica funcionalidad del modulo o fichero creado
from my_module import sumValue, printValue

sumValue(1,2,3)
printValue("Hola Python")

#Python cuenta con varios modulos preinstalados, los cuales se pueden llamar y utilizar
import math

print(math.pi)
print(math.pow(2,8))

from math import pi as PI_VALUE

print(PI_VALUE)