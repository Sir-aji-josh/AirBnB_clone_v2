#!/usr/bin/python3
""" Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exc):
    """ Removes the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """
    Display a HTML page: (inside the tag BODY)
    - displays all Cities in State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    storage.reload()
    app.run(host="0.0.0.0")
