from flask import Flask
from db import selectAllTasks

app = Flask(__name__)


@app.route("/")
# la ruta home
def home():
    taskList = selectAllTasks()
    print(taskList)
    return "<h1>Hola esen</h1>"


if __name__ == "__main__":
    app.run(debug=True)
