from flask import Flask
from controller.book_controller import book_controller

app = Flask(__name__)

app.template_folder = "./view"

app.register_blueprint(book_controller, url_prefix="/book")


app.run(debug=True, host="0.0.0.0", port=8000)
