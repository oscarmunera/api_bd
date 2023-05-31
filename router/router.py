from fastapi import APIRouter

libro = APIRouter()

@libro.get("/")
def root():
    return{"mensaje":"Hola soy una api con un router"}