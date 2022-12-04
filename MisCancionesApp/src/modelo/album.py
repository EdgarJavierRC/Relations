import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    anio = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Medio))
    canciones = relationship('Cancion', secondary='album_cancion')
    minutos = Column(Integer)
    segundos = Column(Integer)
    compositor = Column(String)
    albumes = relationship('Album', secondary='album_cancion')
    interpretes = relationship('Interprete')
