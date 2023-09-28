from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  published_year = db.Column(db.Integer, nullable=False)
  copy_count = db.Column(db.Integer, nullable=False)
  authors = db.relationship('Author', secondary='author_book', backref="books", lazy=True)

  def __repr__(self):
    return f'Book("{self.title}", {self.published_year}, {self.copy_count})'


class Author(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  surname = db.Column(db.String(80), nullable=False)

  def __repr__(self):
    return f'Author("{self.name}", "{self.surname}"'


class AuthorBook(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
