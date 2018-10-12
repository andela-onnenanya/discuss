from sqlalchemy.orm import Session

from Model import Comment, Translation, Language, Category

from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:mat610@localhost/discuss")


session = Session(bind=engine)
# session = sessionmaker(bind=engine)

# init_sqlalchemy()
categories = [
  Category(name='Children'),
  Category(name='Cars'),
  Category(name='Jokes'),
  Category(name='Religion'),
  Category(name='Philosophy'),
  Category(name='Leadership'),
  Category(name='Marriage'),
  Category(name='Cooking'),
  Category(name='Technology'),
  Category(name='Spiritual')
]

languages = [
  Language(name='Spanish', code="SP"),
  Language(name='French', code='FR'),
  Language(name='German', code='GR')
]

comments = [
  Comment(comment='I know what I am doing!', category_id=6, score=0),
  Comment(comment='I want to pupu!', category_id=1, score=0),
  Comment(comment='Toyota is my best car', category_id=2, score=0),
  Comment(comment='I love shits', category_id=3, score=0),
  Comment(comment='He is a devoted man', category_id=4, score=0),
  Comment(comment='Wishes are not horses', category_id=5, score=0),
  Comment(comment='My wife is my best friend', category_id=7, score=0),
  Comment(comment='I love Nigeria jollof', category_id=8, score=0),
  Comment(comment='You have to learn the version 12.3.0', category_id=9, score=0),
  Comment(comment='I can see the hidden things of your mind', category_id=10, score=0),
  Comment(comment='This is just an extra joke', category_id=3, score=0)
]

translations = [
  Translation(translation='Js affsdf meea takaf sf', comment_id=1, language_id=1),
  Translation(translation='Int pas me de vo', comment_id=1, language_id=2),
  Translation(translation='Yusss maytt tos', comment_id=1, language_id=3),
  Translation(translation='JIngro dosh', comment_id=2, language_id=1),
  Translation(translation='Maya na dos viszoz', comment_id=2, language_id=2),
  Translation(translation='Jytto pa senta', comment_id=2, language_id=3),
]

session.bulk_save_objects(categories)
session.bulk_save_objects(languages)
session.bulk_save_objects(comments)
session.bulk_save_objects(translations)
session.commit()
