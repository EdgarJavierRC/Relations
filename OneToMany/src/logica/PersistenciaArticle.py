from src.modelo.Article import Article
from src.modelo.Comment import Comment
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.declarative_base import session

class PersistenciaArticle():
    def agregarArticle(self, titulo):
        busqueda = session.query(Article).filter(Article.titulo == titulo).all()
        if len(busqueda) == 0:
            article = Article(titulo=titulo)
            session.add(article)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        articles = session.query(Article).all()
        print('\n### Articulos:')
        for article in articles:
            print(f'id: {article.id} Título: {article.titulo}')
        print('')

    def eliminarFilaAFila(self):
        articles = session.query(Article).all()
        for article in articles:
            session.delete(article)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from articles"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla articles")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Article).get(id)