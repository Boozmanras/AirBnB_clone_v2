#!/usr/bin/python3
"""Flask web application to display states and their cities"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close_storage(exception):
    """Close the current SQLAlchemy session"""
    storage.close()

@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """Display a HTML page with a list of states or a specific state"""
    states = storage.all('State')
    if id:
        state = states.get('State.' + id)
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', states=states.values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
