# Exercício 1

# Usando o banco de dados trybnb devidamente carregado via container:

#     Realize uma busca por todos os imóveis que se localizam na Espanha
#     ordenados, de forma crescente, pelo atributo _id;
print("RESP: db.places.find({'address.country': 'Spain'}).sort({'_id': 1})")

#     Realize uma busca por todos os imóveis que se localizam nos Estados
#     Unidos que retorne a quantidade de imóveis.
print("RESP: db.places.find({'address.country': 'United States'}).count()")

# DICA: No banco os nomes dos países estão armazenados em inglês, ou seja, no
# caso da Espanha estará Spain e no caso dos Estados Unidos estará United
# States.
