class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} fazendo som")


class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} amamentando")


class Cachorro(Mamifero):
    def latir(self):
        print(f"{self.nome} faz au au!")


cachorro = Cachorro("Rex")
cachorro.fazer_som()  # Rex fazendo som
cachorro.amamentar()  # Rex amamentando
cachorro.latir()  # Rex faz au au!
