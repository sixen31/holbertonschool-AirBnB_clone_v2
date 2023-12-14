#!/usr/bin/python3
"""
    Script that start a flask application and list of states.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    The function `state_list` retrieves a list of states
    from storage and renders a template with the
    list of states.
    :return: the rendered template "7-states_list.html"
    with the variable "list_states" set to the value
    of the "states" variable.
    """
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)


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
