#!/usr/bin/python3
"""Flask web application to display states and cities"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close_storage(exception):
    """Close the current SQLAlchemy session"""
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    """Display a HTML page with a list of states and cities"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
