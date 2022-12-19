#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, abort, render_template
import models
from models.amenity import Amenity
from models.city import City
from models.state import State


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all_states():
    """ This function loads all cities of states"""
    states = models.storage.all(State).values()
    cities = models.storage.all(City).values()
    amenities = models.storage.all(Amenity).values()
    return render_template(
                           '10-hbnb_filters.html',
                           states=states,
                           cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """ Remove current SQLAlchemy Session """
    models.storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
