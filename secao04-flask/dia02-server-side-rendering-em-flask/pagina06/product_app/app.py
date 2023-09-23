from flask import Flask
from controllers.products_controller import products_controller

app = Flask(__name__)

app.static_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/product_app/view/static"  # noqa: E501

app.template_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/product_app/view/"  # noqa: E501

app.register_blueprint(products_controller, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True)
