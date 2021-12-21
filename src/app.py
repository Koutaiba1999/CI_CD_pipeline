
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome baby"

@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
