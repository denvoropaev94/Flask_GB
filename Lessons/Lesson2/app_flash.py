from flask import Flask, flash, request, render_template, abort, redirect, url_for

app = Flask(__name__)
app.secret_key = '2a54c85e93c0f024211fbf309545784e7a9751b649d2f8f1e1725dcaeb69bce9'
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hello! This is my site :)'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверяем данные формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
