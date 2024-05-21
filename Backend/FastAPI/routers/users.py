#Modulos a importar del framework
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])

# Entidad user

#BaseModel da la capacidad de crear una entidad.
#Para las API se deben hacer todas las funciones asincronas, para que se siga ejecutando las funciones y enviar mas peticiones al servidor.
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

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Julio", "surname": "Machado", "url": "https://github.com/JulioV93", "age": 30},
            {"name": "Alejandro", "surname": "Vasquez", "url": "https://github.com/AlejandroV93", "age": 34},
            {"name": "vanessa", "surname": "Moncayo", "url": "https://github.com/VanessaV93", "age": 28}]

#Al usar BaseModel como constructor, se indica cual dato es cada uno para que no exista confusión interna, la clase User esta replicando el comportamiento de BaseModel
@router.get("/usersclass")
async def usersclass():
    return User(id_usuario=1,name="Julio",surname="Machado",url="https://github.com/JulioV93",age=30)

@router.get("/users")
async def users():
    return users_list

#Manera de pasar parametros por GET

#1 - PATH
#Se usa el path o ruta de la url para pasar parametros y poder obtener los datos especificos.
#http://127.0.0.1:8000/user/1
@router.get("/user/{id_usuario}")
async def user(id_usuario: int):
    return search_users(id_usuario)

#2 - Query
#Pasar por query es pasar todos los parametros despues del ? y se concatena con & cada parametro
#http://127.0.0.1:8000/userquery/?id_usuario=4&name=Julio
@router.get("/user/")
async def user(id_usuario: int):
    return search_users(id_usuario)

#Manera de utilizar POST
#Se pasa un JSON en el body
#Manejo de codigos de error HTTP
#Manejo de muestra de respuesta en documentación, response_model
@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_users(user.id_usuario)) == User:
        #raise lanza la excepción HTTP, se usa en vez del return
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.routerend(user)
        return user

#Manera de utilizar PUT
#Se pasa un JSON en el body
@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id_usuario == user.id_usuario:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error": "No se ha actualizado el usuario especificado."}
    else:
        return user

#Manera de utilizar DELETE
#Se utiliza a traves de la URL
@router.delete("/user/{id_usuario}")
async def user(id_usuario: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id_usuario == id_usuario:
            del users_list[index]
            found = True 

    if not found:
        return {"error": "No se ha eliminado el usuario especificado."}

def search_users(id_usuario: int):
    users = filter(lambda user: user.id_usuario == id_usuario, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario especificado."}