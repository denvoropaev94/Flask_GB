# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.
from flask import Flask, flash, request, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response('Cookie установлен!')
    response.set_cookie('username','admin')
    return response

@app.route('/getcookie/')
def get_cookies():
    # получаем значения  cookie
    name = request.cookies.get('username')
    return f'Значение cookie: {name}'


if __name__ == '__main__':
    app.run(debug=True)
