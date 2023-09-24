from flask import Flask
from task_model import Task


tasks = [
    Task(1, "estudar", True),
    Task(2, "fazer exercícios", False),
    Task(3, "ler um capítulo", True),
]

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
