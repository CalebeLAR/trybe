# Exercício 4

# Crie e teste, pelo ThunderClient, os endpoints para apagar (DELETE) uma
# piada.

print(
    """
@jokes_controller.route("/<id>", methods=["DELETE"])
DELETE http://localhost:8000/jokes/6508de950889169a580a3585

"DELETE /jokes/6508de950889169a580a3585 HTTP/1.1" 204 -
"""
)
