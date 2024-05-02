### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Julio", "Machado")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Julio"))
print(my_tuple.index("Machado"))
print(my_tuple.index("Julio"))

#Las tuplas son inmutables, es decir, no se pueden modificar despues de asignarle valores
#my_tuple[1] = 1.80 'tuple' object does not support item assignment
print(my_tuple)

#De esta sumatoria o concatenación nace una nueva tupla
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#Se convierte la tupla a lista para manipularla
my_tuple = list(my_tuple)
print(type(my_tuple))

#my_tuple[4] = "JMV"
my_tuple.insert(1, "Verde")
print(tuple(my_tuple))

#Se puede borrar una tupla completa, no se puede por una valor determinado
del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined