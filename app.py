from flask import Flask, render_template, redirect, request
from users import db_user, User, login
from flask_login import current_user

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'a123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db_user.init_app(app)
login.init_app(app)


@app.route("/")
def index():
    db_user.create_all()
    return render_template('index.html')


@app.route("/login")
def login():

    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        user = User(email=email, username=username)
        user.set_password(password)
        db_user.session.add(user)
        db_user.session.commit()
        return redirect('/login')
    else:
      return render_template('register.html')


if __name__ == "__main__":
    app.run()
