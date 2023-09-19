"""
# ...

# 1 - Importe uma nova controller para nossa pagina inicial
# Obs: não se preocupe, implementaremos ela logo a seguir
from controllers.home_controller import home_controller

# ...

# Lembrando: instanciamos o servidor Flask
# app = Flask(__name__)

# 2 - Indique à aplicação onde ficarão nossos arquivos estáticos e templates
app.static_folder = "views/static"
app.template_folder = "views/templates"

# 3 - Registre a nova controller
app.register_blueprint(home_controller, url_prefix="/")

"""