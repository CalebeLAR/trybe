class Pagina04:
    def Utilizando_MongoDB_com_Docker():
        # docker run --name mongodb_v6 -d -p 27017:27017 mongo:6.0

        # https://hub.docker.com/
        pass

    def Executando_o_shell_do_MongoDB_no_Docker():
        # docker exec -it mongodb_v6 mongosh

        # Para mais informações sobre o mongosh, acesse sua documentação
        # https://www.mongodb.com/docs/mongodb-shell/
        pass

    def Importando_uma_base_de_dados_para_o_MongoDB():
        # docker exec mongodb_v6 mongoimport -d trybnb -c places --file /tmp/trybnb.json --jsonArray # noqa: E501

        # docker cp trybnb.json mongodb_v6:/tmp/trybnb.json

        # use trybnb
        # db.places.find()

        # Vamos usar o arquivo .JSON que está disponível neste link
        # https://lms-assets.betrybe.com/lms/trybnb.json

        # Podemos realizar o procedimento de carregar o arquivo JSON para o
        # MongoDB usando a ferramenta mongexport.
        # https://www.mongodb.com/docs/database-tools/mongoexport/
        pass
