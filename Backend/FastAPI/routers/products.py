#Enrutado de APIS con APIRouter
from fastapi import APIRouter

#Manera de declarar el path unico de la API con prefix
#Manera de agrupar la documentación con tags
router = APIRouter(prefix="/products",
                tags=["products"],
                responses={404: {"message": "No encontrado"}})

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/}")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]