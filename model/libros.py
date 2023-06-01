
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, unique=True, index=True)
    autor = Column(String)
    anio_publicacion = Column(Integer, nullable=False)
    genero = Column(String)


