from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user

#BaseModel da la capacidad de crear una entidad.

class User(BaseModel):
    id_usuario: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [
        User(id_usuario=1,name="Julio",surname="Machado",url="https://github.com/JulioV93",age=30),
        User(id_usuario=2,name="Alejandro",surname="Vasquez",url="https://github.com/JulioV93",age=34),
        User(id_usuario=3,name="Vanessa",surname="Moncayo",url="https://github.com/JulioV93",age=28)
        ]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Julio", "surname": "Machado", "url": "https://github.com/JulioV93", "age": 30},
            {"name": "Alejandro", "surname": "Vasquez", "url": "https://github.com/AlejandroV93", "age": 34},
            {"name": "vanessa", "surname": "Moncayo", "url": "https://github.com/VanessaV93", "age": 28}]

#Al usar BaseModel como constructor, se indica cual dato es cada uno para que no exista confusión interna, la clase User esta replicando el comportamiento de BaseModel
@app.get("/usersclass")
async def usersclass():
    return User(id_usuario=1,name="Julio",surname="Machado",url="https://github.com/JulioV93",age=30)

@app.get("/users")
async def users():
    return users_list

#Manera de pasar parametros por GET

#1 - PATH
#Se usa el path o ruta de la url para pasar parametros y poder obtener los datos especificos.
#http://127.0.0.1:8000/user/1
@app.get("/user/{id_usuario}")
async def user(id_usuario: int):
        return search_users(id_usuario)

#2 - Query
#Pasar por query es pasar todos los parametros despues del ? y se concatena con & cada parametro
#http://127.0.0.1:8000/userquery/?id_usuario=4&name=Julio
@app.get("/user/")
async def user(id_usuario: int):
    return search_users(id_usuario)
    
def search_users(id_usuario: int):
    users = filter(lambda user: user.id_usuario == id_usuario, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario especificado."}