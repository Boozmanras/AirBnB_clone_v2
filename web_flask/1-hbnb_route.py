#!/usr/bin/python3
"""A simple Flask web application with multiple routes."""
from web_flask import app

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'."""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
