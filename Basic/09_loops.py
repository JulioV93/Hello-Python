### Loops ###

#While

my_condition = 0

#While se repite en función de una condición y se ejecutara tantas veces se cumpla esa condición
#Python permite aplicar un else cuando no se cumple una condición del while
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecuión continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecuión")
        break #Sirve para romper un ciclo
    print(my_condition)

print("La ejecuión continúa")

#For
#For se ejecutara tantas veces tenga elementos una estructura dada.
#Python permite aplicar un else cuando no se finaliza el recorrido del for

my_list = [35, 24, 62, 52, 30, 30, 17]
print("Lista")
for element in my_list:
    print(element)

print("Tupla")
my_tuple = (35, 1.77, "Julio", "Machado")
for element in my_tuple:
    print(element)

print("Set")
my_set = {"Julio", "Machado", 30}
for element in my_set:
    print(element)

print("Diccionario")
my_dict = {"Nombre":"Julio","Apellido":"Machado","Edad":30,1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para el diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecuión continúa")
