# 1. Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.
# 2. Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма для загрузки изображений.
# 3. Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.
# 4. Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.
# 6. Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.
# 7. Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет выведено введенное число и его квадрат.
import pathlib

from flask import Flask, render_template, request, abort, url_for, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello_mir/')
def hello():
    return "Hello friend!"


@app.route('/download/', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        file = request.files.get('image')
        file_name = secure_filename(file.filename)
        file.save(pathlib.PurePath.joinpath(pathlib.Path.cwd(), 'downloads', file_name))
        return f"Изображение {file_name} успешно загружено на сервер!"
    return render_template('form_images.html')


user = {
    'login': 'denvoropaev',
    'password': '777111'
}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == user['login'] and password == user['password']:
            return f'Hello {login}'
    return render_template('login.html')


@app.route('/area/', methods=['GET', 'POST'])
def area():
    if request.method == 'POST':
        text_area = request.form.get('area')
        len_text = len(text_area.split())
        return f'Количество слов в тексте {len_text}'
    return render_template('text_area.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num_1 = int(request.form.get('num1'))
        num_2 = int(request.form.get('num2'))
        operation = request.form.get('operation')
        if operation == 'add':
            return f'Сумма чисел ={num_1 + num_2}'
        if operation == 'subtract':
            return f'Разность чисел ={num_1 - num_2}'
        if operation == 'multiply':
            return f'Произведение чисел ={num_1 * num_2}'
        if operation == 'divide' and num_2 != 0:
            return f'Частное чисел ={num_1 / num_2}'
    return render_template('calc_form.html')


@app.errorhandler(403)
def age_error(e):
    app.logger.error(e)
    context = {
        'title': 'возрастные ограничения',
        'url': request.base_url,
    }
    return render_template('403.html', **context), 403


@app.route('/age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age < 18:
            abort(403)
        return f'Добро пожаловать {name} - {age} лет(года)'
    return render_template('fio.html')


@app.route('/redirect/')
def redirect_to():
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
