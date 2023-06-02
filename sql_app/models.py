from sqlalchemy import Column,Integer,String
from sql_app.database import Base

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    anio_publicacion = Column(Integer)
    genero = Column(String)