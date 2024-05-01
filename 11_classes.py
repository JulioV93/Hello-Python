### Classes ###

#Por buenas practicas se utliza la primera letra de la palabra en Mayusucla, sin espacios y guioones
class MyEmptyPerson:
	pass

print(MyEmptyPerson)
print(MyEmptyPerson())

#def __init__(self) es un constructor de clase y es obligatorio al realizar una clase.
class Person:
	#Constructor o declaración de propiedades del objeto.
	def __init__(self, name, surname, alias = "Sin alias"):
		#Al self, que es la misma clase, se le estan asignando las propiedades name y surname los parametros name y surname respectivamente.
		self.full_name = f"{name} {surname}, ({alias})"

		#Se estan declarando llos parametros como provados, no se pueden acceder y modificar.
		self.__name = name
		self.__surname = surname
		self.__alias = alias

	#Declaración de los metodos o funciones del objeto.
	#Se recomienda dejar las propiedades como privadas y acceder a ellas con los metodos
	def get_name(self):
		return self.__name

	def get_surname(self):
		return self.__surname

	def get_alias(self):
		return self.__alias		

	def walk(self):
		print(f"{self.full_name} esta caminado")

my_person = Person("Julio", "Machado")
print(f"{my_person.get_name()} {my_person.get_surname()}")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Julio", "Machado", "JulioMV93")
print(f"{my_person.get_name()} {my_person.get_surname()}")
print(my_other_person.full_name)
my_other_person.walk()

#Se puede acceder a una clase y propiedad de ella y modificarla despues de que se instancie, es decir despues de crearla.
my_other_person.full_name = "Brais Moure (MoureDev)"
print(my_other_person.full_name)

#Hay que tener cuidado con el tipado del lenguaje!
my_other_person.full_name = 666
print(my_other_person.full_name)
