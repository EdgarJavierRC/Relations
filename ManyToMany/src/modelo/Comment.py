from sqlalchemy import Column, Integer, ForeignKey, String
from .declarative_base import Base

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comentario = Column(String, nullable=False)
    article_id = Column(Integer, ForeignKey('articles.id'))
