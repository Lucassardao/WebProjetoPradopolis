from flask import Flask, render_template

#criar a instancia do flask
app = Flask(__name__,template_folder='static/templates')

#criar a rota
@app.route('/')

def index():
    return render_template("index.html")