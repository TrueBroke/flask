from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return '<h1>О нас</h1>'

@app.route('/contact')
def contact():
    return '<h1>Наши контакты</h1>'

@app.route('/user')
@app.route('/profile')
def user_profile():
    return '<h1>Профиль пользователя</h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'<h1>Профиль пользователя: {username}</h1>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'<h1>Пост №{post_id}</h1>'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'<h1>Подпуть: {subpath}</h1>'

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    
    def save(self):
        # Сохранение в БД
        pass
    
    def get_by_id(cls, id):
        # Получение из БД
        pass
if __name__ == "__main__":
    app.run(debug=True)