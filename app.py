from flask import Flask, render_template
app = Flask(__name__)

log = []

@app.route('/')
def hello():
    return render_template("index.html", content="Home")

@app.route('/view')
def view():
    output = ""

    for s in log:
        output += s + "<br>"

    return render_template("view.html", logoutput=log)

@app.route('/write/<content>')
def write(content=None):
    log.append(content)
    return(content)