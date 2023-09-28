import datetime

from flask import Flask, render_template, jsonify
from Lessons.Lesson3.models_02 import db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../../instance/mydatabase.db'
# app. config['SQLALCHEMY_DATABASE_URI' ] = 'mysql+pymysql: / /username: password@hostname/db_name'
# app. config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:/ /username: password@hostname/db_name'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_users(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]
        )
    else:
        return jsonify({'error': 'Posts not found'}), 404


@app.route('/posts/last-week/')
def get_posts_by_author():
    date = datetime.utcnow() - datetime.timedelta(days=7)
    posts = Post.query.filter_by(Post.created_at >= date).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]
        )
    else:
        return jsonify({'error': 'Posts not found'}), 404


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@mail.ru')
    db.session.add(user)
    db.session.commit()
    print('John add in DB')


@app.cli.command('edit-john')
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@gmail.com'
    db.session.commit()
    print('Edit John mail in DB!')


@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username='User5').first()
    db.session.delete(user)
    db.session.commit()
    print('DElete john from DB')


@app.cli.command('fill-db')
def fill_tables():
    count = 5
    #   добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}email.ru')
        db.session.add(new_user)
    db.session.commit()
    #     добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
