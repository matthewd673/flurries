from flask import Flask, render_template, request
from flask.helpers import get_template_attribute, url_for

from datetime import datetime
import time

app = Flask(__name__)

class Message:
    def __init__(self, message, category, timestamp):
        self.message = message
        self.category = category

        self.timestamp = timestamp

class State:
    def __init__(self, property, current_state, timestamp):
        self.property = property
        self.current_state = current_state
        self.timestamp = timestamp

log = []
long_log = []
states = []

@app.route('/')
def hello():
    return render_template("index.html", content="Home")

@app.route('/view/')
def view():
    output = render_template("view.html", logoutput=log)
    return output

@app.route('/view/raw/')
def view_raw():
    return render_template("view-raw.html", rawoutput=long_log)

@app.route('/log/<message>')
def log_basic(message=None):
    return write_log(message, "log")

@app.route('/log/error/<message>')
def log_error(message=None):
    return write_log(message, "error")

@app.route('/log/warn/<message>')
def log_warn(message=None):
    return write_log(message, "warn")

@app.route('/log/highlight/<message>')
def log_highlight(message=None):
    return write_log(message, "highlight")

@app.route('/log/state/<property>/<current_state>/')
def log_state(property=None, current_state=None):
    update_state(property, current_state)

def write_log(message, category):
    new_log = Message(message, category, get_timestamp())
    long_log.insert(0, "[" + category + "] " + message + " (" + new_log.timestamp + ")")
    log.insert(0, new_log)
    return message

def update_state(property, current_state):
    timestamp = get_timestamp()
    for s in states:
        if(s.property == property):
            s.current_state = current_state
            s.timestamp = timestamp
            return property + ": " + current_state
    
    new_state = State(property, current_state, get_timestamp())
    states.append(new_state)
    return property + ": " + current_state

def get_timestamp():
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time

@app.route('/poll/')
def poll_update():
    while(len(log) == 0):
        time.sleep(0.5)
    output = render_template("log-item.html", logoutput=log)
    log.clear()
    return output

@app.route('/poll/state/')
def poll_state_update():
    while(len(states) == 0):
        time.sleep(0.1)
    output = render_template("state-item", stateoutput=states)
    return output