from flask import Flask


app = Flask(__name__)


@app.get('/')
def root():
    return 'Hello world!'


@app.get('/about/')
def about():
    return 'About!'


@app.get('/contacts/')
def contacts():
    return 'Contacts!'


@app.get('/calc/<int:number_1>/sum/<int:number_2>')
def calc_sum(number_1, number_2):
    summa = number_1 + number_2
    return f'{number_1} + {number_2} = {summa}'

@app.get('/str_len/<string:text>')
def str_len(text):
    return f'The string "{text}" includes {len(text)} symbols'


@app.get('/html')
def html():
    text = """
        <h1>Моя первая HTML страница</h1>
        <p>Привет, мир!</p>
    """

    return text


if __name__ == '__main__':
    app.run(debug=True)