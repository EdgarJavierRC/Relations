import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base
from sqlalchemy import
from .declarative_base import Base

album = Column(Integer, ForeignKey('album.id'))


class AlbumCancion(Base):
    __tablename__ = 'album_cancion'

    album = Column(Integer, ForeignKey('album.id'), primary_key=True)
    cancion = Column(Integer, ForeignKey('cancion.id'), primary_key=True)

    canciones = relationship('cancion', secondary='album_cancion')


