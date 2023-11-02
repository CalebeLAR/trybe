from flask import Flask
from home_controller import home_controller

app = Flask(__name__)
app.static_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/movies_app/views/"  # noqa: E501
app.template_folder = "/home/ca3ele/Desktop/trybe/secao04-flask/dia02-server-side-rendering-em-flask/pagina06/movies_app/views"  # noqa: E501

app.register_blueprint(home_controller, url_prefix="/")


app.run(debug=True, host="0.0.0.0", port=8000)
