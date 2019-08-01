# Flask 
Flask is a micro web framework written in Python. It is classified as a microframework
because it does not require particular tools or libraries. It has no database abstraction
layer, form validation, or any other components where pre-existing third-party libraries 
provide common functions.

# Dependencies
These distributions will be installed automatically when installing Flask.
 1. Werkzeug implements WSGI, the standard Python interface between applications and servers.
 2. Jinja is a template language that renders the pages your application serves.
 3. MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
 4. ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
 5. Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

# Create a virtual environments
sudo apt-get install python-virtualenv
1. $ mkdir foldername
2. $ cd foldername
3. $ virtualenv -p python3 .
4. $ source bin/activate
5. $ pip install flask
