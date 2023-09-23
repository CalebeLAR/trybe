from flask import Flask
from products_controller import products_controller
# from procucts_model import Product

app = Flask(__name__)

app.register_blueprint(products_controller, url_prefix="/")


if __name__ == "__main__":
    app.run()
