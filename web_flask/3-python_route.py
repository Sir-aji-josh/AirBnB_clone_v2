#!/usr/bin/python3
""" Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ a function that returns the string 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ a function that returns the string 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    a function that display 'C' followed by the value
    of the text variable.
    """
    return "C " + str(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
def python_default_text():
    """ Displays the python route default string.
    """
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    a function that displays 'Python',
    followed by the value of the text variable
    """
    return "Python " + str(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')


