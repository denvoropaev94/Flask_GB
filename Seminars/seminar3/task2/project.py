from flask import Flask, render_template, request
from models import db, Book, Author, AuthorBook
from logging import getLogger as Logger


app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
  db.create_all()
  print('OK')


@app.cli.command("fill-db")
def fill_tables():
  count = 5

  for number in range(1, count):
    book = Book(title=f'book_{number}', published_year=1997+number, copy_count=1+number)
    db.session.add(book)
    db.session.commit()

  for number in range(1, count):
    author = Author(
      name=f'name_{number}',
      surname=f'surname_{number}'
    )
    db.session.add(author)
    db.session.commit()

  db.session.add(AuthorBook(author_id=1, book_id=1))
  db.session.add(AuthorBook(author_id=2, book_id=1))

  db.session.add(AuthorBook(author_id=2, book_id=2))
  db.session.add(AuthorBook(author_id=3, book_id=2))
  db.session.add(AuthorBook(author_id=4, book_id=2))

  db.session.add(AuthorBook(author_id=5, book_id=3))
  db.session.add(AuthorBook(author_id=1, book_id=4))
  db.session.add(AuthorBook(author_id=2, book_id=5))

  db.session.commit()


@app.get('/')
def home():
  context = {'books': Book.query.all()}
  return render_template('home.html', **context)


@app.errorhandler(404)
def page_not_found(e):
  logger.warning(e)

  context = {
    'title': 'Page not found =(',
    'url': request.referrer,
  }
  return render_template('404.html', **context), 404
