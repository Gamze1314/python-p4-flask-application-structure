#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__) # __name__ refers to the name of the current module to be interpreted as Flask application.


@app.route('/')  # decorator. we call functions that map to URLs views. view returns the response. in other words, we are binding / URL to the index() function.
def index(): # app.route decorator registers index() to the application instance.(app)
    return '<h1>Welcome to my page!</h1>'


@app.route('/<string:username>') # username is string w angle brackets, <>, parameter.
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)


# to run flask server => through Werkzeug or this is another way of running the Flask application.

#Werkzeug 
# run_simple(
#     hostname='localhost',
#     port=5555,
#     application=application
# )  or;


# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask run  => flask run and flask shell looks for app.py by default.


#or;

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)  and run the script.
