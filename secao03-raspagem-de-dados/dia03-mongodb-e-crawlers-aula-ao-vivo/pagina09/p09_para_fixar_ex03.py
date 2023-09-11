# Para fixar
# Exercício 3

# Usando o banco de dados trybnb…
#     Altere a hospedagem de _id “12”, para que seu campo review_scores_rating
#     receba nota de 65;

print(
    """RESP:
trybnb> db.places.find({_id: 12}, {'review_scores.review_scores_rating': true})
[ { _id: 12, review_scores: { review_scores_rating: 75 } } ]

trybnb> db.places.updateOne({_id: 12}, {$set: {'review_scores.review_scores_rating': 65}})  # noqa
    {
       acknowledged: true,
       insertedId: null,
       matchedCount: 1,
       modifiedCount: 1,
       upsertedCount: 0
    }

trybnb> db.places.find({_id: 12}, {'review_scores.review_scores_rating': true})
[ { _id: 12, review_scores: { review_scores_rating: 65 } } ]

"""
)

#     Altere todas as hospedagens do host “José Edmílson” para que ele tenha o
#     campo host_identity_verified como true;
print(
    """
RESP:
trybnb> db.places.updateMany({'host.host_name': 'José Edmílson'}, {$set: {'host.host_identity_verified': true}}) # noqa
    {
    acknowledged: true,
    insertedId: null,
    matchedCount: 2,
    modifiedCount: 1,
    upsertedCount: 0
    }
"""
)
