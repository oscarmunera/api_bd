from pydantic import BaseModel
from typing import Optional

class LibroSchema(BaseModel):
    id: Optional[int] = None
    titulo:str
    autor:str
    anio_publicacion:int
    genero:str