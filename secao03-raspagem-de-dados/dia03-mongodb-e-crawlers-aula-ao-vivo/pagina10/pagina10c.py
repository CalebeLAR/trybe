class Pagina10:
    def Método_Delete():
        # Método deleteOne(): Para deletar apenas um documento;
        # Método deleteMany(): Para deletar vários documentos.
        pass

    def deleteOne():
        # db.places.deleteOne({ _id: 11 })
        pass

    def deleteMany():
        # remove todos os documentos que tenham valor do campo
        # host.host_identity_verified como false.
        # db.places.deleteMany({ "host.host_identity_verified": { $eq: false }}) # noqa

        # O comando abaixo remove todos os documentos da coleção
        # db.places.deleteMany({})
        pass

    pass
