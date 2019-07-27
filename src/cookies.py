"""
A cookie is stored on a client’s computer in the form of a text file. 
Its purpose is to remember and track data pertaining to a client’s 
usage for better visitor experience and site statistics.
"""
from flask import (
	Flask, 
	request,
	render_template, 
	make_response
	)
app = Flask(__name__)

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
	if request.method == 'POST':
		user=request.form['nm']

	resp = make_response(render_template('readcookie.html'))
	resp.set_cookie('userID', user)
	return resp

@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userID')
	return '<h1>Welcome '+name+'</h1>'

if __name__ == '__main__':
	app.run(debug=True)