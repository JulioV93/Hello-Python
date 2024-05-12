from fastapi import FastAPI

app = FastAPI()

print(app)

#Siempre que llamamos a un servidor, la operación debe ser asincrona.

#La asincronia hace que se deba esperar por que la operación termine y la aplicación pueda continuar haciendo otras tareas mientras se termine la operación solicitada.

#uvicorn es un modulo de servidor que disponibiliza FastAPI, trabaja en 127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url_curso":"https://github.com/JulioV93"}