### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for i in range(101):
        #Se debe empezar por el caso mas restrictivo un if.
        if i%5 == 0 and i%3 == 0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama(string_1, string_2):
    #Estamos validando que no sean palabra iguales, si son iguales por defecto es falso.
    #Se pueden comparar las palabras todas en minusculas o todas en mayusculas.
    if string_1.lower() == string_2.lower():
        return False
    
    #sorted retorna una lista, en este caso estamos ordenando la palabra, si las 2 palabras ordenadas dan el mismo valor es verdadero
    return sorted(string_1.lower()) == sorted(string_2.lower())

print(is_anagrama("Amor", "ramo"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1
    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

#Si un numero se divide entre un numero que no sea uno y el mismo, y el residuo da 0, quiere decir que no es primo
def is_prime():
    for number in range(1,101):
        if number >= 2:
            is_divisible = False
            
            for index in range(2, number):

                #El operador % busca el modulo o residuo de una división
                if number % index == 0:
                    is_divisible = True
                    break
                
            if not is_divisible:
                print(number)
            
is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

#Manera de ordenar al revez una palabra sin utilizar funciones epecificas del lenguaje.
def reverse(string):
    text_len = len(string)
    reversed_string = ""
    for i in range(0, text_len):
        reversed_string += string[text_len - i -1]
        
    print(reversed_string)
    print(string[::-1])


reverse("Hola mundo")