from flask import Flask, render_template

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


@app.get('/students/')
def students():
    students = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'age': 20,
            'avg_mark': 4.9
        },
        {
            'name': 'Ivan',
            'surname': 'Kuznecov',
            'age': 21,
            'avg_mark': 5.0
        },
        {
            'name': 'Ivan',
            'surname': 'Sidorov',
            'age': 19,
            'avg_mark': 4.8
        }
    ]
    return render_template('students.html', students=students)


@app.get('/news/')
def news():
    news = [
        {
            'title': 'Новый 2023 Год!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '01.01.2023'
        },
        {
            'title': 'C 8 Марта!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '08.03.2023'
        },
        {
            'title': 'C Днем Программиста!',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt, fugit.',
            'published_at': '13.09.2023'
        },
    ]

    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
