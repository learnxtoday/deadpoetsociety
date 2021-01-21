from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/wibble')
def wibble():
    return 'This is my pointless new page'
