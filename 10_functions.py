### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

#Al indicar el tipo de dato, puede servir como referencia de lo que se necesita para que la función funcione de mejor manera.
def sum_two_values(first_value: int,second_value: int):
    print(first_value + second_value)

sum_two_values(5,7)
sum_two_values(54754,71231)
sum_two_values("5","7")
sum_two_values(1.4,5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4,5.2)
print(my_result)    

my_result = sum_two_values_with_return(10,5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Machado", name = "Julio")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname}, {alias}")

print_name_with_default("Julio", "Machado")
print_name_with_default("Julio", "Machado", "JulioMV93")

#El asterisco permite enviar todo los parametros que se necesiten de manera indefinida, es decir el numero de parametros es dinamicos.
def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "JulioMV93")
print_upper_texts("Hola")