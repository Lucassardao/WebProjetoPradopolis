from flask import Flask, render_template

#criar a instancia do flask
app = Flask(__name__)

#criar a rota
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def index_1():
    return render_template("index.html")

@app.route("/registro.html")
def registro():
    return render_template('registro.html')