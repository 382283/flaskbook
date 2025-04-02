from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"],endpoint="endpoint-name")
def index():
    return "Hello, Flaskbook!"

@app.route("/hello/<name>",methods=["GET", "POST"],endpoint="hello-endpoint")
def hello(name):
    return render_template("index.html", name=name)

