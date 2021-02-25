# to init manually -> $env:FLASK_APP = "server.py" (windows) -> flask run
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', name=home)


@app.route('/dojade')
def jak_dojade():
    return render_template('dojade.html', name=jak_dojade)


@app.route('/info')
def info():
    return render_template('info.html', name=info)


@app.route('/o_nas')
def o_nas():
    return render_template('onas.html', name=o_nas)


@app.route('/rejestracja')
def rejestracja():
    return render_template('rejstracja.html', name=rejestracja)


if __name__ == '__main__':
    app.run()
