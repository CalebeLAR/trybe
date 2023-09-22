from flask import Flask
from src.controllers.home_controller import home_controller


# app
app = Flask(__name__)

# folders
app.template_folder = "src/views/templates"

# routers
app.register_blueprint(home_controller, url_prefix="/home")

# server
app.run(debug=True, host="0.0.0.0", port=8000)
