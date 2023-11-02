class Pagina09:
    def Método_Update():
        # Método updateOne(): Para alterar apenas um valor;
        # Método updateMany(): Para alterar vários valores.

        # Aqui vale a pena citar o caso do Airbnb, no qual foi baseada essa
        # lição!
        # https://noticias.uol.com.br/internacional/ultimas-noticias/2019/05/23/familia-morta-no-chile-airbnb-estava-em-predio-sem-certificado-de-gas.htm
        pass

    def updateOne_e_updateMany():
        # Sintaxe do updateOne com o $set: atualiza um valor
        # db.places.updateOne({<filtro>}, {$set: {<updadted value>}})
        # trybnb> db.places.updateOne({_id: 13}, {$set: {description: 'essa casa tem o id 13'}}) # noqa

        # Sintaxe do updateOne com o $unset: remove um valor
        # db.places.updateOne({<filtro>}, {$unset: {<removed value>}})
        # trybnb> db.places.updateOne({_id: 13}, {$unset: {description: 'essa casa tem o id 13'}}) # noqa

        # Sintaxe do updateMany com o $set: atualiza todos os valores do filtro
        # db.places.updateMany({<filtro>}, {$set: {<updadted value>}})
        # trybnb> db.places.updateMany({_id: {$gte: 13}}, {$set: {isFree: true}}) # noqa

        # Sintaxe do updateMany com o $unset: remove atualiza todos os valores do filtro # noqa
        # db.places.updateMany({<filtro>}, {$unset: {<removed value>}})
        # trybnb> db.places.updateMany({_id: {$gte: 13}}, {$unset: {isFree: true}}) # noqa

        # db.places.updateMany({_id: {$gte: 13}},{$set: {isFree: true}})
        pass

    def Para_fixar():
        pass

    def Exercício03():
        pass

    pass
