#!/usr/bin/python3
"""
Script that starts a Flask web application and displays a page similar to 6-index.html
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    The function `hbnb_filters` retrieves a list of states, cities, and amenities
    from storage and renders a template with the
    content similar to 6-index.html.
    :return: the rendered template "10-hbnb_filters.html"
    with the variables "states", "cities", and "amenities" set to the values
    of the corresponding variables.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    cities = sorted(list(storage.all(City).values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all(Amenity).values()), key=lambda x: x.name)
    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)


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
