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
