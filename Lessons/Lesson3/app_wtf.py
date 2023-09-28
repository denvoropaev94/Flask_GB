from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'6df8358ab39a9cdc88287fbacba0375c516943569e0cbd26d36721bbd80e5b44'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hi'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
