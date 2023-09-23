from flask import Blueprint, render_template
from models.procucts_model import Product


products_controller = Blueprint("products_controller", __name__)


def get_first_list_products():
    list_procucts = [
        {"name": "Smartphone", "price": 799.99},
        {"name": "Notebook", "price": 1299.99},
        {"name": "Televisor", "price": 499.99},
        {"name": "Liquidificador", "price": 89.99},
        {"name": "Máquina de Lavar Roupa", "price": 699.99},
        {"name": "Refrigerador", "price": 899.99},
        {"name": "Aspirador de Pó", "price": 129.99},
        {"name": "Forno de Micro-ondas", "price": 149.99},
        {"name": "Secadora de Roupas", "price": 499.99},
        {"name": "Cafeteira Elétrica", "price": 69.99},
    ]

    products = []
    for _id, product in enumerate(list_procucts):
        products.append(Product(_id, product["name"], product["price"]))

    return products


@products_controller.route("/", methods=["GET"])
def get_products():
    products = get_first_list_products()
    return render_template("product.html", products=products)


@products_controller.route("/", methods=["PUT"])
def put_products():
    return "bota produto"
