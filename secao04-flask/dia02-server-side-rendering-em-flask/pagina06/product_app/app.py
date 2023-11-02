from operator import methodcaller
from flask import Flask, render_template, request, redirect
from procucts_model import Product

app = Flask(__name__)
products = []


app.static_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/product_app/view/static"
app.template_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/product_app/view/templates"


@app.route("/", methods=["GET"])
def products_view():
    return render_template("products.html", products=products)


@app.route("/", methods=["POST"])
def add_product():
    _id = len(products) + 1
    name = request.form.get("name")
    price = float(request.form.get("price"))
    new_product = Product(_id, name, price)
    products.append(new_product)
    return render_template(products=new_product)


@app.route("/delete/<int:product_id>")
def delete_product(product_id):
    for product in products:
        if product.id == product_id:
            products.remove(product)
            break
    return redirect("/")


if __name__ == "__main__":
    app.run()
