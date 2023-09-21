import pathlib
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello! This is my site :)'


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name} !'
    return render_template('form.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(pathlib.PurePath.joinpath(pathlib.Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} успешно загружен на сервер!"
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
