from flask import Flask, request, make_response, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '2a54c75e93c0f024211fbf309545784e7a9751b649d2f8f1e1725dcaeb69bce9'


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        context = {
            'name': name,
            'email': email
        }
        response = make_response(render_template('name.html', **context))
        response.set_cookie('username', name)
        return response
    return render_template('login.html')


@app.route('/delcookie/')
def delete_cookie():
    res = make_response(render_template('login.html'))
    res.set_cookie('username', '', max_age=0)
    return res


if __name__ == '__main__':
    app.run(debug=True)
