from flask import Flask, render_template
from flask.helpers import url_for
app = Flask(__name__)

class Message:
    def __init__(self, message, category):
        self.message = message
        self.category = category

log = []

@app.route('/')
def hello():
    return render_template("index.html", content="Home")

@app.route('/view')
def view():
    output = []

    return render_template("view.html", logoutput=log)

@app.route('/log/<message>')
def log_message(message=None):
    new_log = Message(message, "log")
    log.append(new_log)
    return "❄ " + message

@app.route('/log/error/<message>')
def log_error(message=None):
    new_log = Message(message, "error")
    log.append(new_log)
    return "🛑 " + message

@app.route('/log/warn/<message>')
def log_warn(message=None):
    new_log = Message(message, "warn")
    log.append(new_log)
    return "⚠ " + message