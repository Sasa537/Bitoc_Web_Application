from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():

    return "This is index page our web application"


if __name__ == "__main__":
    app.run()
