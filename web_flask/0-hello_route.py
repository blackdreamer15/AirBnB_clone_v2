from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def root():
  """Returns the string: Hello HBNB!"""
  return "Hello HBNB!"

if __name__ == "__name__":
  app.run(host='0.0.0.0', port=5000)
