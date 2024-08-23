#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
