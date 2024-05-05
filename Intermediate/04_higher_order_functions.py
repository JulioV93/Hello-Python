### Higher Order Functions ###

from functools import reduce

#Son funciones que hacen cosas con funciones, son ciudadanos de primera clase.

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value):
    return  sum_one(first_value + second_value)

print(sum_two_values_and_one(5, 2))

#Se puede pasar una función como parametro
def sum_two_values_and_one(first_value, second_value, f_sum):
    return  f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

### Closures ###
#Funcion que difine una función y retorna una función
#Es la posibilidad de retornar funciones
def sum_ten():
    def add(value):
        return  value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

def sum_ten(original_value):
    def add(value):
        return  value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))
print((sum_ten(5))(1))

### Buit-in Higher Order Functions ###

number = [2, 5, 10, 21, 3, 30]

#Map -> Con un listado iterable retorna el resultado de la ejecuión de una función para cada uno de los elementos del listado original.
#Hace sentido usar map con las funciones lambda, de ejecución de procesos cortos

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, number)))
print(list(map(lambda number: number * 2, number)))

#Filter -> Con un listado iterable retorna el resultado de la ejecuión de una función para cada uno de los elementos del listado original.
#Ejcuta un filtro dado a travez de una función
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, number)))
print(list(filter(lambda number: number > 10, number)))

#Reduce -> Con un listado iterable retorna el resultado de la ejecuión de una función para cada uno de los elementos del listado original.
#Va sumando los valores de la lista, hasta reducirlo a un unico valor
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, number))
print(reduce(lambda first_value, second_value: first_value + second_value, number))