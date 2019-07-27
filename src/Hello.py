from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World'

# Variable rules
@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return "Blog number %d" % postID	

@app.route('/rev/<float:revNo>')
def revision(revNo):
	return "Revision no %f" % revNo


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)	