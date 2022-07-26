from flask import Flask, render_template
from users import db_user

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'a123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db_user.init_app(app)


@app.route("/")
def index():
    db_user.create_all()
    return render_template('index.html')


@app.route("/login")
def login():

    return render_template('login.html')


@app.route("/registr")
def reg():

    return render_template('registr.html')


if __name__ == "__main__":
    app.run()
