from flask import Flask 
app = Flask(__name__)

@app.route('/flask') # 127.0.0.1:5000/flask/ won't work
def hello_flask():
	return "hello_flask"

@app.route('/python/') # 127.0.0.1:5000/python will work fine
def  hello_python():
	return "hello_python"

if __name__ == '__main__':
	app.run()