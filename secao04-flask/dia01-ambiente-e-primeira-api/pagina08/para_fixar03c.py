# Exercício 3

# Utilize o ThunderClient para criar e testar os endpoints necessários para
# realizar uma atualização (PUT) em uma piada.

print(
    """
@jokes_controller.route("/<id>", methods=["PUT"])
GET http://localhost:8000/jokes/6508de950889169a580a3585
{
  "joke": "joke 4 update"
}
{
  "_id": "6508de950889169a580a3585",
  "joke": "joke 4 update"
}
    """
)
