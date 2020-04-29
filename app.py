import os
from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt
from os import path
if path.exists("env.py"): 
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'login_example'
app.config['MONGO_URI'] = os.environ['MONGO_URI']

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login')
def login():
        return ''

@app.route('/register')
def register():
        return ''

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)