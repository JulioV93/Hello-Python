### File Handling ###
# HAY QUE TENER CUIDADO EN WINDOWS CON LA CARPETA ONEDRIVE
#Se debe ejecutar en una capeta raiz con todos los permisos.

import os

# .txt file

"""  
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
"""
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write("Mi nombre es Julio\nMi apellido es Machado\nMi edad es 30\nMi lenguaje favorito es Python")
#En el primer print se consumo todo el archivo, por eso al segundo print se ve vacio porque no hay caracteres para leer
#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline(10))
print(txt_file.readlines(10))

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta PHP")
print(txt_file.readline())

#Siempre se debe cerrar el archivo con el que se trabaja.
txt_file.close()

#with permite cerrar el archivo despues de su lectura o escritura, se recomienda siempre cerrar el archivo.
with open('Intermediate/my_file.txt', "a") as f:
    f.write("\nY Java")

#os.remove("Intermediate/my_file.txt")

# .json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name":"Julio",
    "surname":"Machado",
    "age":30,
    "languages":["Python", "PHP", "Java"],
    "website":"https://github.com/JulioV93"}

json.dump(json_test, json_file, indent=4)
    
json_file.close()

#Al momento de leer archivos JSON se pueden manerar como diccionarios manejan como diccionarios

with open('Intermediate/my_file.json') as f:
    for line in f.readlines():
        print(line)
        
json_dict = json.load(open("Intermediate/my_file.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["name"])
for line in json_dict:
    print(line)
    
# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languages", "website"])
csv_writer.writerow(["Julio", "Machado", 30, "Python", "https://github.com/JulioV93"])
csv_writer.writerow(["Roswell", "", 2, "Java", ""])

csv_file.close()

with open('Intermediate/my_file.csv') as f:
    for line in f.readlines():
        print(line)
# .xlsx file
# import xlrd Hay que investigar sobre este modulo.

# .xml file

import xml