from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

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