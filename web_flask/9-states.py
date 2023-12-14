#!/usr/bin/python3
"""
Script that starts a Flask web application and lists states and their cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """
    The function `states_list` retrieves a sorted list of states
    from storage and renders a template with the
    sorted list of states.
    :return: the rendered template "9-states.html"
    with the variable "states" set to the value
    of the "states" variable.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_cities(id):
    """
    The function `state_cities` retrieves the state and its cities
    from storage and renders a template with the
    state and its cities.
    :param id: the id of the state
    :return: the rendered template "9-states.html"
    with the variable "state" set to the value
    of the "state" variable.
    """
    state = storage.get(State, id)
    if state is None:
        return render_template("9-states.html", state=None)
    return render_template("9-states.html", state=state)


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
