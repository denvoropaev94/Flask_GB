from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, everybody!!!'


@app.route('/users/')
def users():
    _users = [{'name': 'Den',
               'mail': 'denvoropaev@gmail.com',
               'phone': '+375298988279',
               },
              {'name': 'Nik',
               'mail': 'denv@gmail.com',
               'phone': '+3752989453279',
               },
              {
                  'name': 'Oleg',
                  'mail': 'wrepaev@gmail.com',
                  'phone': '+37529898423525',
              }, ]
    context = {'users': _users,
               'title': 'Точечная нотация'}

    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
