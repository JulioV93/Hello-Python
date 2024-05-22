#Los schemas ayudan a tener funciones para las consultas a la bbdd, para transformar los datos de bbdd a una estructura que se pueda trabajar
def user_schema(user) -> dict:
    return {"_id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}
    
def users_schema(users) -> list:
    return [user_schema(user) for user in users]