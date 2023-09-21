from flask import Flask, flash, request, render_template, abort, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '2a54c75e93c0f024211fbf309545784e7a9751b649d2f8f1e1725dcaeb69bce9'


@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
