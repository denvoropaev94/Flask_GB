from flask import Flask, render_template, request
from models import db, Faculty, Student
from logging import getLogger as Logger

app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 5

    for number in range(1, count + 1):
        faculty = Faculty(title=f'faculty_{number}')
        db.session.add(faculty)
        db.session.commit()

        for student_number in range(1, count + 1):
            student = Student(
                name=f'name_{student_number}',
                surname=f'surname_{student_number}',
                age=22 + count,
                gender='male',
                group_number=f'{number}_{12}',
                faculty_id=number
            )
            db.session.add(student)
            db.session.commit()


@app.get('/')
def home():
    context = {'students': Student.query.all()}
    return render_template('home.html', **context)


@app.errorhandler(404)
def page_not_found(e):
  logger.warning(e)

  context = {
    'title': 'Page not found =(',
    'url': request.referrer,
  }
  return render_template('404.html', **context), 404
