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


@app.route("/number/<int:n>", strict_slashes=False)
def is_n_a_number(n):
    """Returns "n is a number" only if n is an integer"""
    return f"{n:d} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Returns a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
