from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud
import models 
import schemas
from schemas import LibroBase
from database import SessionLocal, engine


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#@app.get("/libros/", response_model=list[schemas.LibroBase])
#def read_libros(skip: int = 0, limit: int =100, db: Session = Depends(get_db)):
#    libros = crud.get_libros(db, skip=skip, limit=limit)
 #   return libros

@app.get("/libros/{libro_id}", response_model=schemas.LibroBase)
def read_libro(libro_id: int, db: Session = Depends(get_db)):
    libros = crud.get_libro(db, libro_id=libro_id)
    print (Session.__name__)
    if libros is None:
        raise HTTPException(status_code=404, detail="User not found")
    return libros