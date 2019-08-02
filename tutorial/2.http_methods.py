from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

"""
HTTP Methods
--------------------------------
GET     -> requests are used to retreive data from a server at the specified resource
POST    -> requests are used to send data to the API sever to create or udpate a resource (non-idempotent).
PUT     -> requests are used to send data to the API to create or update a resource.
HEAD    -> an effective way of simply verifying that a resource is available. 
DELETE  -> delete the resource at the specified URL.
PATCH   -> only apply partial modifications to the resource (non-idempotent).
OPTIONS -> return data describing what other methods and operations the server supports at the given URL.

An idempotent method means that the result of a successful performed request is independent of the number of times it is executed.
"""
