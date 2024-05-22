### User DB API ###
#Se replico el CRUD de users.py, y se ejecuto la misma tarea con la conexión a MongoDB

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                tags=["userdb"],
                responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

#Se usa ObjectID para setear el id que se recibe porque en la bbdd es un objeto lo que se almacena, no un string plano.
@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))

@router.get("/")
async def user(id: str):
    return search_user("_id", ObjectId(id))

#Insert a la BBDD
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

#Update a la BBDD
@router.put("/", response_model=User)
async def user(user: User):
    print(user)
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario especificado."}
    
    return search_user("_id", ObjectId(user.id))

#Delete a la BBDD
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    
    if not found:
        return {"error": "No se ha eliminado el usuario especificado."}

#Operación de busqueda para los listados
def search_user(field: str, key):
    try:
        user = user_schema(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "No se ha encontrado el usuario especificado."}