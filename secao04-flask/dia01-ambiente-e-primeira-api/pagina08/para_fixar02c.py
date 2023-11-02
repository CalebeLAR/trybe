# Exercício 2

# Utilize o ThunderClient para criar e testar os endpoints necessários para
# realizar as solicitações de tipo GET disponíveis na rota /jokes.

print(
    """
@jokes_controller.route("/", methods=["GET"])
GET http://localhost:8000/jokes
[
  {
    "_id": "6508d76cf38baa96d88d48e9",
    "joke": "Por que o bombeiro não gosta de andar? <br> Porque ele socorre."
  },
  {
    "_id": "6508db061b71bd72a7c4e91c",
    "joke": "Por que o bombeiro não gosta de andar? <br> Porque ele socorre."
  }
]

@jokes_controller.route("/random", methods=["GET"])
GET http://localhost:8000/jokes/random
{
  "_id": "6508db061b71bd72a7c4e91c",
  "joke": "Por que o bombeiro não gosta de andar? <br> Porque ele socorre."
}


@jokes_controller.route("/<id>", methods=["GET"])
GET http://localhost:8000/jokes/6508d76cf38baa96d88d48e9
{
  "_id": "6508d76cf38baa96d88d48e9",
  "joke": "Por que o bombeiro não gosta de andar? <br> Porque ele socorre."
}



"""
)
