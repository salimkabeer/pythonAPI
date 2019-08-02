# Flask
Flask is a lightweight WSGI web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex 
applications. It began as a simple wrapper around Werkzeug and Jinja and has 
become one of the most popular Python web application frameworks.

# How to create virtual environment
1. sudo apt-get install python3-venv or vertualenv
2. mkdir folder
3. cd folder
4. python3 -m venv venv
5. source bin/activate
6. pip3 install flask (click, Werkzeug, jinja2, itsdangerous, MarkupSafe)

# How to run flask apps
* $ export FLASK_APP=hello.py
* $ export FLASK_DEBUG=1
* $ flask run (OR python -m flask run)


# To enable all development features
* It will enable the debugger, automatic reloader
* $ export FLASK_ENV=development
* $ flask run

# To initialize database
* $ flask init-db

# To install the project
* $ create MANIFEST.in
* $ pip install -e .