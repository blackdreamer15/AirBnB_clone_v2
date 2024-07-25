from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def root():
  return "Hello HBNB!"

if __name__ == "__name__":
  app.run()
