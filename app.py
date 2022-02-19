from flask import Flask

app = Flask(__name__)


@app.route("/")
# la ruta home
def home():
    return "<h1>Hola esen</h1>"


if __name__ == "__main__":
    app.run(debug=True)
