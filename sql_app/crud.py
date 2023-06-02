from sqlalchemy.orm import Session
from sql_app import models

def get_libro(db: Session, libro_id: int):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()

def get_libros(db: Session, skip: int=0,limit: int=100):
    return db.query(models.Libro).offset(skip).limit(limit).all()

