from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

#JWT controla de manera automatica el tiempo restante para la expiración del token
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "A5s454scfaSDAsd65454DD"

router = APIRouter(prefix="/jwtauth",
                tags=["jwtauth"],
                responses={404: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

#Los esquemas definen el algoritmo de encriptación
crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

#Las contraseñas sse encriptaron aqui -> https://bcrypt-generator.com
users_db = {
    "JulioMV93": {
        "username": "JulioMV93",
        "full_name": "Julio Machado",
        "email": "julio.machadov93@gmail.com",
        "disabled": False,
        "password": "$2a$12$YN52AEMvEfOoH//3LzS1dOPU2ZGkCEoxLmfH/rP.jDTmDONVV2avS"
    },
    "JulioMV932": {
        "username": "JulioMV932",
        "full_name": "Julio Machado 2",
        "email": "julio.machadov932@gmail.com",
        "disabled": True,
        "password": "$2a$12$kaEjR6Uqbvtya3gTQguZzOShUtYP.0JEZ4XfIVLPXVISp8qa9nYEq"
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
    
#Se obtiene el token y se desencripta
async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales de autenticación inválidas",
                headers={"WWW-Authenticate": "Bearer"})
    
    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo",
            headers={"WWW-Authenticate": "Bearer"})
        
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = search_user_db(form.username)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    #Se inicia el conteo de duaración del token que se genera.
        
    access_token = {"sub":user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    
    #retornamos un access token, esto es un estandar para no tener que iniciar sesión en cada petición, por lo que se solicita solamente el token retornado para validarlo.
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user