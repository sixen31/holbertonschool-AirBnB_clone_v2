#!/usr/bin/python3
"""Script that start a flask application and list of states"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """The function `state_list` retrieves a list of state"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def handle_teardown(exc):
    """The function "handle_teardown" is used to close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
