from flask import Blueprint, render_template

home_controller = Blueprint("home_controller", __name__)

data = [
    "O Poderoso Chefão",
    "O Senhor dos Anéis: O Retorno do Rei",
    "Cidadão Kane",
    "A Lista de Schindler",
    "O Touro Indomável",
    "Forrest Gump",
    "Pulp Fiction",
    "O Silêncio dos Inocentes",
    "Interestelar",
    "Jurassic Park",
    "O Resgate do Soldado Ryan",
    "Gladiador",
]


@home_controller.route("/", methods=["GET"])
def home():
    return render_template("index.html", data=data)
