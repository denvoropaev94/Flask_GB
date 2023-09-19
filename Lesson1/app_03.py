from flask import Flask

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Денис</h1>
<p>Я не так давно начал изучать Flask.</br>Посмотрите на мой сайт)</p>
"""

@app.route('/')
def hello():
    return 'Hello, everybody!!!'

@app.route('/text/')
def text():
    return html

@app.route('/poems/')
def poems():
    poem = ['Вот не думал не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык!',
            ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '</br>'.join(poem) + '</p>'
    return txt



if __name__ == '__main__':
    app.run(debug=True)