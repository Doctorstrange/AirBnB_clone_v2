#!/usr/bin/python3
"""script starts a Flask web application"""

from flask import Flask

app = Flask("__name__")


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """web application must be listening on 0.0.0.0, port 5000"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
