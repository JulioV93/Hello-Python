### Conditionals ###

my_condition = False

#Por defecto el if acepta la condición como True
if my_condition:
	print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
	print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:
	print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
	print("Es igual a 25")
else:
	print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecuión continúa")

my_string = ""

#Un string vacio lo considera False
if not my_string:
	print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoo":
	print("Estas cadenas de textos coinciden")