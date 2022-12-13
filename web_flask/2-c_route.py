#!/usr/bin/python3
"""
This script starts a Flask web application:
this web application is listening on 0.0.0.0, port 5000
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ /: display “Hello HBNB!” """
    """ /hbnb: display “HBNB” """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    """
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
