#!/usr/bin/python3
"""
Initialization of Flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Returns "C" followed by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is_cool"):
    """Returns "Python" followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
