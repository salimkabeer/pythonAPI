from flask import Flask
app = Flask(__name__) # WSGI application on current single module

@app.route('/') # decorator to tell Flask what URL should trigger our function.
def hello_world():
    return 'Hello, World!'
    
"""
---------------------------------
Routing the path

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
---------------------------------
Variable Rules

string  -> (default) accepts any text without a slash
int     -> accepts positive integers
float   -> accepts positive floating point values
path    -> like string but also accepts slashes
---------------------------------
Unique URLs / Redirection Behavior

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about') # 404 “Not Found” error if called without "/"
def about():
    return 'The about page'
---------------------------------
"""
