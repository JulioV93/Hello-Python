from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user

#BaseModel da la capacidad de crear una entidad.

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    
users_list = [
        User(name="Julio",surname="Machado",url="https://github.com/JulioV93",age=30),
        User(name="Alejandro",surname="Vasquez",url="https://github.com/JulioV93",age=34),
        User(name="Vanessa",surname="Moncayo",url="https://github.com/JulioV93",age=28)
        ]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Julio", "surname": "Machado", "url": "https://github.com/JulioV93", "age": 30},
            {"name": "Alejandro", "surname": "Vasquez", "url": "https://github.com/AlejandroV93", "age": 34},
            {"name": "vanessa", "surname": "Moncayo", "url": "https://github.com/VanessaV93", "age": 28}]

#Al usar BaseModel como constructor, se indica cual dato es cada uno para que no exista confusión interna, la clase User esta replicando el comportamiento de BaseModel
@app.get("/usersclass")
async def usersclass():
    return User(name="Julio",surname="Machado",url="https://github.com/JulioV93",age=30)

@app.get("/users")
async def users():
    return users_list