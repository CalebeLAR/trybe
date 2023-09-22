from flask import Flask
from controllers.home_controller import home_controller

app = Flask(__name__)

app.static_folder = "/view/static"
app.template_folder = "/view/templates"

app.register_blueprint(home_controller, url_prefix="/")


app.run(debug=True, host="0.0.0.0", port=8000)
