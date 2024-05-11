### Regular Expressions ###

#Ayuda a visualizar si una cadena de texto tiene ciertos elementos.
#Se debe studiar las expreciones regulares mas a detalle, Hector de Leon tiene clases de expreciones regulares.

#Puede servir para buscar un xssClean como en PHP, esto para limpiar los inputs y que no se realice inyección de código.

import re

my_string = "Esta es la lección numero 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección npumero 6: Manejo de ficheros"

# match

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span())
print(type(match.span()))
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
#if not(match == None):
#if match != None:
if match is not None:
    print(match)
    print(match.span())
    print(type(match.span()))
    start, end = match.span()
    print(my_other_string[start:end])
    
print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("lección", my_string, re.I)
print(search)
print(search.span())
print(type(search.span()))
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)
print(type(findall))

# split

split = re.split(":", my_string)
print(split)
print(type(split))

# sub
sub = re.sub("Expresiones Regulares", "RegEx", my_string, re.I)
print(sub)
print(type(sub))

sub = re.sub("lección|Lección", "LECCIÓN", my_string, re.I)
print(sub)
sub = re.sub("[l|L]ección", "LECCIÓN", my_string, re.I)
print(sub)

# Patterns https://regex101.com
#La r es reservado para python y sirve para escribir espreciones regulares

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.search(pattern, my_string))
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "julio.machadov93@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))