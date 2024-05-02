### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Julio","Apellido":"Machado","Edad":30,1:"Python"}

#Dentro de un diccionario de pueden almacenar otros diccionarios o cualquier tipo de dato y estructura.
my_dict = {
    "Nombre":"Julio",
    "Apellido":"Machado",
    "Edad":30,
    "Lenguajes": {"Python","Swift","Kotlin"},
    1:1.68
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict.get('Calle')) #Si no existe la clave, get permite que no aparezca error, trayendo un NoneType

#Manera de modificar un valor de una clave en especifico
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "La Siembra"
print(my_dict)

#Si se le pasa del al diccionario solo, este lo borrara por completo
del my_dict["Calle"]
print(my_dict)

#Se esta confirmando si eciste una clave dentro del diccionario.
print('Nombre' in my_dict) # True
print('Pedro' in my_dict) # False

print(my_dict.items()) #Retorna una lista de tuplas
print(my_dict.keys()) #Retorna una lista con las claves
print(my_dict.values()) #Retorna una lista con los valores que tienen las claves
print(my_dict.fromkeys(("Nombre", 1))) #Crea un diccionario con las claves indicadas, sin valores asignados

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
print(type(my_new_dict))

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
print(type(my_new_dict))

#Esta es la forma correcta de crear un diccionario reutilizando las claves de otro diccionario
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
print(type(my_new_dict))

my_new_dict = dict.fromkeys(my_dict, ("JMV"))
print(my_new_dict)
print(type(my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))

#Hay que tomar en cuenta que en un lenguaje fuertemente tipado no se pudieran hacer estas modficiaciones.
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
