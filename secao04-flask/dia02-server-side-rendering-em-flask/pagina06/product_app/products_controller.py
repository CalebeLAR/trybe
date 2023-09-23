from flask import Blueprint


products_controller = Blueprint("products_controller", __name__)


@products_controller.route("/", methods=["GET"])
def get_products():
    return "toma os produto"


@products_controller.route("/", methods=["PUT"])
def put_products():
    return "bota produto"
