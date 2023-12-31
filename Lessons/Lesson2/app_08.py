from flask import Flask, request, render_template, abort, redirect, url_for
from Lessons.Lesson2.db import get_blog

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello! This is my site :)'


@app.route('/hello/<name>/')
def hello(name):
    return f'Hello {name}!'


@app.route('/redirect/<name>/')
def redirect_hello(name):
    return redirect(url_for('hello'))


@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.get('/submit/')
def submit_get():
    return render_template('form.html')


@app.post('/submit/')
def submit_post():
    name = request.form.get('name')
    return f'Hello, {name}!'


@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    # делаем запрос в БД для поиска статьи по id
    result = get_blog(id)
    if result is None:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_not_found(e):
    app.logger.error(e)
    context = {
        'title': 'Ошибка сервера',
        'url': request.base_url,
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)
