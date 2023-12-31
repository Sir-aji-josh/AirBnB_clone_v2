#!/usr/bin/python3
""" A script thats starts a Flask web application.
"""
from flask import Flask

app = Flask(_name_)


# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if _name_ == '_main_':
    # Run the web application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)

