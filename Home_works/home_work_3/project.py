from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from logging import getLogger as Logger
from registration_form import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
app.config['SECRET_KEY'] = '2a54c75e93c0f024211fbf309545784e7a9751b649d2f8f1e1725dcaeb69bce9'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.get('/')
def home():
    context = {'users': User.query.all()}
    return render_template('home.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        hash_pswd = generate_password_hash(form.password.data)
        user = User(
            full_name=form.full_name.data,
            e_mail=form.e_mail.data,
            password=hash_pswd
        )
        db.session.add(user)
        db.session.commit()

        response = make_response(redirect(url_for('home')))
        flash('Успешная регистрация!', 'success')
        return response
    else:
        return render_template('register.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)

    context = {
        'title': 'Page not found =(',
        'url': request.referrer,
    }
    return render_template('404.html', **context), 404
