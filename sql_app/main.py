from fastapi import Depends,FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud
from sql_app import models
from sql_app import LibroBase
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/libros/", response_model=list[models.Libro])
def read_libros(skip: int = 0, limit: int =100,db:Session=Depends(get_db)):
    libros =crud.get_libros(db,skip=skip,limit=limit)
    return libros