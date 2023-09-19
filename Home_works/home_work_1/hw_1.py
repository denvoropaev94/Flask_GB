# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
from flask import Flask, render_template

app = Flask(__name__)


@app.get('/')
def root():
    return render_template('home.html')

@app.get('/about/')
def about():
    return 'HOME WORK 1'


@app.get('/shoes/')
def shoes():
    shoes = [
        {
            'id': '001',
            'type': 'Oxfords',
            'price': 20,
            'year_issue': 2022
        },
        {
            'id': '002',
            'type': 'Loafers',
            'price': 2000,
            'year_issue': 2023
        },
        {
            'id': '003',
            'type': 'Moccasins',
            'price': 100,
            'year_issue': 2019
        }
    ]
    context = {'shoes': shoes,
               'title': 'New shoes'}

    return render_template('shoes.html', **context)


@app.get('/cloth/')
def cloth():
    cloth = [
        {
            'id': '001',
            'gender': 'female',
            'type': 'underwear',
            'name': 'Aston Martin',
            'price': 200
        },
        {
            'id': '002',
            'gender': 'female',
            'type': 'underwear',
            'name': 'Colins',
            'price': 10
        },
        {
            'id': '003',
            'gender': 'male',
            'type': 'underwear',
            'name': 'Ferrari',
            'price': 20
        }
    ]
    context = {'cloth': cloth,
               'title': 'New cloth'}

    return render_template('cloth.html', **context)



@app.get('/jackets/')
def jackets():
    jackets = [
        {
            'id': '001',
            'type': 'Windbreakers',
            'price': 20,
            'year_issue': 2022
        },
        {
            'id': '002',
            'type': 'Bombers',
            'price': 2000,
            'year_issue': 2023
        },
        {
            'id': '003',
            'type': 'Harringtons',
            'price': 100,
            'year_issue': 2019
        }
    ]
    context = {'jackets': jackets,
               'title': 'New jackets'}

    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
