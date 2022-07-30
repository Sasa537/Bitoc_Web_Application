from flask import Flask, render_template, redirect, request, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from users import db_user, User, login
from flask_login import current_user

app = Flask(__name__)
UPLOAD_FOLDER = 'static/avatars/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'a123456789'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db_user.init_app(app)
login.init_app(app)


@app.route("/")
def index():
    #db_user.create_all()
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
        id_btc = request.form['id_btc']
        file = request.files['file']

        user_email = User.query.get(email)
        if user_email is not None:
            flash('This Email is already use')
            print(user_email)
            return redirect(request.url)
        if email == "":
            flash('No Email')
            return redirect(request.url)
        if username == "":
            flash('No Username')
            return redirect(request.url)
        if password == "":
            flash('No Password')
            return redirect(request.url)

        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            avatar = "/avatars/"+filename

            user = User(email=email, username=username, id_btc=id_btc, avatar=avatar)
            user.set_password(password)
            db_user.session.add(user)
            db_user.session.commit()
            return redirect('/login')
    else:
      return render_template('register.html')


if __name__ == "__main__":
    app.run()
