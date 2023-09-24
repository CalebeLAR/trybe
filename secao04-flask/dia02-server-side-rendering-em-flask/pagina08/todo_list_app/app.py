from flask import Flask, Blueprint, render_template, request
from task_model import Task


tasks = [
    Task(1, "estudar", True),
    Task(2, "fazer exercícios", False),
    Task(3, "ler um capítulo", True),
]

app = Flask(__name__)

app.static_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina08/todo_list_app/view/static"  # noqa: E501
app.template_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina08/todo_list_app/view/templates"  # noqa: E501

tasks_controller = Blueprint("tasks_controller", __name__)


@tasks_controller.route("/", methods=["GET"])
def render_tasks():
    return render_template("tasks.html", tasks=tasks)


@tasks_controller.route("/", methods=["POST"])
def add_tasks():
    new_id = len(tasks) + 1
    new_task = request.form.get("nova-tarefa")
    tasks.append(Task(new_id, new_task, False))
    return render_template("tasks.html", tasks=tasks)


@tasks_controller.route("/complete/<int:task_id>", methods=["GET"])
def completed_tasks(task_id):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.remove(task)
            task.completed = not bool(task.completed)
            tasks.insert(i, task)

    return render_template("tasks.html", tasks=tasks)


app.register_blueprint(tasks_controller, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
