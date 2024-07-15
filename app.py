from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def kaligan():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/katha')
def katha():
    return render_template('katha.html')