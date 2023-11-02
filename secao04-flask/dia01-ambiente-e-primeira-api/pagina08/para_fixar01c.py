#  Exercício 1

# Utilize o ThunderClient para acessar o endpoint /jokes e realizar uma
# solicitação para criação (POST) de uma piada.

print(
    "RESP:\n"
    "POST http://localhost:8000/jokes\n"
    "{\n"
    '   "joke": "Por que o bombeiro não gosta de andar? <br> Porque ele socorre."\n'  # NOQA (E501)
    "\n}",
)
