from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def root():
  return "Hello HBNB!"
