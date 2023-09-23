from flask import Blueprint, jsonify, render_template, request
from models.procucts_model import Product


products_controller = Blueprint("products_controller", __name__)


products_db = [
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


def get_first_list_products():
    products = []
    for _id, product in enumerate(products_db):
        products.append(Product(_id, product["name"], product["price"]))

    return products


@products_controller.route("/", methods=["GET"])
def get_products():
    products = get_first_list_products()
    return render_template("product.html", products=products)


@products_controller.route("/", methods=["POST"])
def put_products():
    product_name = request.form.get("product_name")
    product_price = request.form.get("product_price")
    product = Product(len(products_db), product_name, product_price)
    products_db.append(product)
    return render_template("product.html", products=products_db)


@products_controller.route("/", methods=["DELETE"])
def delete_products():
    product_name = request.form.get("")
    product_price = request.form.get("product_price")
    product = Product(len(products_db), product_name, product_price)
    products_db.append(product)
    return render_template("product.html", products=products_db)
