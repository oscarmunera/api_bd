from pydantic import BaseModel
from typing import Optional

class LibroBase(BaseModel):
    id: Optional[int] 
    titulo:str
    autor:str
    anio_publicacion:int
    genero:str