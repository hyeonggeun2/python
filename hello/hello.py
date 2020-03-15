from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/user/<name>")
def user(name):
    return render_template('index.html', name=name)

app.run()
