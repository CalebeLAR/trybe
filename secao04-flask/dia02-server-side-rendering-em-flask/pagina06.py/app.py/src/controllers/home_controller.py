from flask import Blueprint, render_template

# controller
home_controller = Blueprint("home", __name__)


# routers
@home_controller.route("/", methods=["GET"])
def index():
    message_prop = "BOAS VINDAS"
    return render_template("index.html", message_prop=message_prop)
