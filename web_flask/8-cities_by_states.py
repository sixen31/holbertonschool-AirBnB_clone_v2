#!/usr/bin/python3
"""
Script that starts a Flask web application and lists cities by states.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    The function `cities_by_states` retrieves a sorted list of states
    and their cities from storage and renders a template with the
    sorted list of states and their cities.
    :return: the rendered template "8-cities_by_states.html"
    with the variable "states" set to the value
    of the "states" variable.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def handle_teardown(exc):
    """
    The function "handle_teardown" is used to close the storage.
    :param exc: The "exc" parameter is short for "exception"
    and is used to handle any exceptions that
    may occur during the teardown process
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
