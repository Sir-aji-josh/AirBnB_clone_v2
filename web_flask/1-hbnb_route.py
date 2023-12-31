#!/usr/bin/python3
""" Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ A function that returns the string 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ A function that returns the string 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")


