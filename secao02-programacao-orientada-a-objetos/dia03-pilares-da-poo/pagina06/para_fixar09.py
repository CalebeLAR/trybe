#  Exercício 9

# Crie a seguinte estrutura:
#  Uma classe Produto com os atributos nome e preco e os métodos descrever
#  e preco;
#  Uma classe Livro que herda de Produto e tem os mesmos atributos da
#  superclasse mais o atributo autor e os métodos descrever e preco;
#  Uma classe DVD que herda de Produto e tem os mesmos atributos da
#  superclasse mais o atributo diretor e os métodos descrever e preco.


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco

    def descrever(self):
        pass

    def preço(self):
        pass


class Livro(Produto):
    def __init__(self, nome: str, autor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.autor = autor

    def descrever(self):
        return f"{self.nome} por {self.autor}"

    def preço(self):
        return self.preco


class DVD(Produto):
    def __init__(self, nome: str, diretor: str, preco: float) -> None:
        super().__init__(nome, preco)
        self.diretor = diretor

    def descrever(self):
        return f"{self.nome} dirigido por {self.diretor}"

    def preço(self):
        return self.preco
