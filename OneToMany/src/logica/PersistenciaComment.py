from src.modelo.Article import Article
from src.modelo.Comment import Comment
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import Session, engine, Base, session

class PersistenciaComment():
    def agregarComment(self, comentario):

        if len(comentario) > 0:
            comment = Comment(comentario=comentario)
            session.add(comment)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        comments = session.query(Comment).all()
        print('\n### Comentarios:')
        for comment in comments:
            print(f'id: {comment.id} Comentario: {comment.comentario} del artículo 1: {comment.article_id}')
        print('')

    def eliminarFilaAFila(self):
        comments = session.query(Comment).all()
        for comment in comments:
            session.delete(comments)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from comments"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla comments")
            print("Nro de registros borrados : ", data_source.rowcount)

    def dar_id(self, id):
        return session.query(Comment).get(id)