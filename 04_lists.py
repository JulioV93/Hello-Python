### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Julio", "Machado"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Machado"))
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3],
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list) TypeError

#Inserta un elemento en la lista
my_other_list.append("JMV")
print(my_other_list)

#Inserta un elemento en la lista, en la posición indicada
my_other_list.insert(1, "Verde")
print(my_other_list)

my_other_list[1] = "Amarillo"
print(my_other_list)

#Remueve un valor indicado
my_other_list.remove("Amarillo")
print(my_other_list)

my_list.remove(30)
print(my_list)

#Elimina el ultimo valor de la lista, y retorna el valor eliminado
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

#Elimna un dato especificado por el indice que se quiere borrar
del my_list[2]
print(my_list)

#Copia una lista indicada
my_new_list = my_list.copy()

#Borra la lista indicada
my_list.clear()
print(my_list)
print(my_new_list)

#Dala vuelta al orden de la lista indicada
my_new_list.reverse()
print(my_new_list)

#Ordena la lista indicada, pero bajo un parametro dado, si no se le da nada, ordena de menor a mayor
my_new_list.sort()
print(my_new_list)

#Python al no se ru lenguaje fuertemente tipado, permite el cambio de tipo de dato
my_list = "Hola Python"
print(my_list)
print(type(my_list))