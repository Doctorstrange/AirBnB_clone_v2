#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """web application must be listening on 0.0.0.0, port 5000"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """web application must be listening on 0.0.0.0, port 5000"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def cplace(text):
    """display “C ” followed by the value of the text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def piithon(text='is cool'):
    """display “Python ”, followed by the value of the text variable """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def numbers(n):
    """display “C ” followed by the value of the text"""
    if isinstance(n, int):
        return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
