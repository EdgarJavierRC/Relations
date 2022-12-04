from src.modelo.Article import Article
from src.modelo.Comment import Comment
from src.modelo.declarative_base import session
from src.logica.PersistenciaArticle import PersistenciaArticle
from src.logica.PersistenciaComment import PersistenciaComment

def almacenar():
    persistenciaArticle = PersistenciaArticle()
    persistenciaComment = PersistenciaComment()
    persistenciaArticle.eliminarFilaSQL()
    persistenciaComment.eliminarFilaSQL()

    # crear Article
    article1 = Article(titulo="Aplicaciones de ML en medicina")
    article2 = Article(titulo="Ingeniería de software ágil")
    session.add(article1)
    session.add(article2)
    session.commit()

    # crear Comment
    comment1 = Comment(comentario="Es un artículo de revisión")
    comment2 = Comment(comentario="Buen artículo")
    session.add(comment1)
    session.add(comment2)
    session.commit()

    # Relacionar articulos con commentarios
    article1.comments = [comment1]
    article2.comments = [comment2]
    session.commit()

    persistenciaArticle.VerFilas()
    persistenciaComment.VerFilas()

    session.close()

def almacenarPersitencia():

    persistenciaArticle = PersistenciaArticle()
    persistenciaComment = PersistenciaComment()
    persistenciaArticle.eliminarFilaSQL()
    persistenciaComment.eliminarFilaSQL()

    # crear Article
    persistenciaArticle.agregarArticle(titulo="Aplicaciones de ML en medicina")
    persistenciaArticle.agregarArticle(titulo="Ingeniería de software ágil")

    # crear Comment
    persistenciaComment.agregarComment(comentario="Es un artículo de revisión")
    persistenciaComment.agregarComment(comentario="Buen artículo")

    # Relacionar articulos con commentarios
    article1 = persistenciaArticle.dar_id(1)
    article2 = persistenciaArticle.dar_id(2)
    comment1 = persistenciaComment.dar_id(1)
    comment2 = persistenciaComment.dar_id(2)

    article1.comments = [comment2]
    article2.comments = [comment1]
    session.commit()

    persistenciaArticle.VerFilas()
    persistenciaComment.VerFilas()

    session.close()

if __name__ == '__main__':
   #almacenar()
   almacenarPersitencia()


