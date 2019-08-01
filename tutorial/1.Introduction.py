from flask import Flask
app = Flask(__name__) # WSGI application on current single module

@app.route('/') # decorator to tell Flask what URL should trigger our function.
def hello_world():
    return 'Hello, World!'
    
"""

"""
