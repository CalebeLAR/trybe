class Pagina08:
    def Operadores_de_Consulta_em_Arrays():
        pass

    def Sifrão_all():
        # Sintaxe do operador $all: busca documentos que contenham todos os valores do array # noqa
        # db.places.find({ amenities: { $all: ["Stove", "Refrigerator"] } })

        # buscar por $all é diferente de buscar por:
        # db.places.find({ amenities: ["Garagem", "jacuzzi", "Armários", "piscina"] }) # noqa
        pass

    def Sifrão_elemMatch():
        # Sintaxe do operador $elemMatch:
        #   busca documentos que contenham ao menos um dos valores do array
        # forma extendida:
        # trybnb> db.places.find({amenities: {$elemMatch: {$in: ["TV"]}}}, {_id:true, amenities: true}) # noqa
        # forma resumida:
        # trybnb> db.places.find({amenities: {$in: ["TV"]}}, {_id:true, amenities: true}) # noqa

        pass

    pass
