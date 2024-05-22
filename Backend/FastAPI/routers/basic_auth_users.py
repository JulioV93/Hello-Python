#Modulo de seguridad de fastAPI -> fastapi.security
#OAuth2PasswordBearer -> Se encarga de gestionar la autetinficación del usuario y contraseña
#OAuth2PasswordRequestForm -> Se encarga de la forma en la que se envian desde el cliente el usaurio y la contraseña y la forma en que la API los recibe

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/basicauth",
                tags=["basicauth"],
                responses={404: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "JulioMV93": {
        "username": "JulioMV93",
        "full_name": "Julio Machado",
        "email": "julio.machadov93@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "JulioMV932": {
        "username": "JulioMV932",
        "full_name": "Julio Machado 2",
        "email": "julio.machadov932@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        #Los ** asi atribución de que se pueden enviar varios parametros
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        #Los ** asi atribución de que se pueden enviar varios parametros
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
        
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo",
            headers={"WWW-Authenticate": "Bearer"})
        
    return user

#Ejemplo de login, se indica que se van a obtener el usuario y ocntraseña por un formulario
@router.post("/login_basic")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    #retornamos un access token, esto es un estandar para no tener que iniciar sesión en cada petición, por lo que se solicita solamente el token retornado para validarlo.
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users_basic/me")
async def me(user: User = Depends(current_user)):
    return user