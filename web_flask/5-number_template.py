#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """display “C ” followed by the value of the text"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numtemp(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)