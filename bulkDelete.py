from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


from Model import Comment, Translation, Language, Category

engine = create_engine("postgresql://postgres:mat610@localhost/discuss")
session = Session(bind=engine)

session.query(Comment).delete()
session.query(Category).delete()
session.query(Translation).delete()
session.query(Language).delete()
session.execute("ALTER SEQUENCE languages_id_seq RESTART WITH 1")
session.execute("ALTER SEQUENCE categories_id_seq RESTART WITH 1")
session.execute("ALTER SEQUENCE comments_id_seq RESTART WITH 1")
session.execute("ALTER SEQUENCE translations_id_seq RESTART WITH 1")
session.commit()