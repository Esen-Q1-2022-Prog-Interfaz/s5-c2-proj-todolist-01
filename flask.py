from flask import Flask

app = Flask(__name__)

# la ruta home
@app.route("/")
def home():
    return "<h1>Hola esen</h1>"
