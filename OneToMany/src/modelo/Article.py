from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base
from src.modelo.Comment import Comment

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    comments = relationship("Comment")