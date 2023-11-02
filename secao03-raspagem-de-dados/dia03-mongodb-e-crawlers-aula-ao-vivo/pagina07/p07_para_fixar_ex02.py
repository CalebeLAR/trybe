# Exercício 2

# Usando o banco de dados trybnb devidamente carregado via container:

#  Realize a inserção de três documento na coleção places que contenham os
#  atributos _id, name e description utilizando o método insertMany();

# DICA 01: No campo _id utiliza valores iguais ou maiores de 100 para evitar
# conflito com registros existentes.

# DICA 02: Nos campos name e description pode-se utilizar valores aleatórios.
# O que é esperado de você é saber utilizar os métodos de inserção
# independente dos valores utilizados.


print(
    "RESP:\n"
    "trybnb> db.places.insertMany([\n"
    "   {_id: 13, name: 'casa na terra', description: 'decrição casa na terra'},\n" # noqa E507
    "   {_id: 14, name: 'outra casa na terra mas com o id 14', description: 'decrição outra casa na terra mas com o id 14',},\n" # noqa E507
    "   {_id: 15, name: 'outra casa na terra', description: 'decrição outra casa na terra'},\n" # noqa E507
    "   {_id: 16, name: 'casa em jupter', description: 'decrição casa em jupter'},\n" # noqa E507
    "])"
) # noqa E507
