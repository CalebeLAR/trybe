class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} fazendo som")


class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} amamentando")


# usasse uma terceira classe para se fazer o Mixin
class Cachorro(Mamifero):
    def latir(self):
        print(f"{self.nome} faz au au!")


class MixinCorrer:
    def correr(self, velocidade):
        print(f"{self.nome} correndo a {velocidade} km/h")


class CachorroCorredor(Cachorro, MixinCorrer):
    pass


cachorro = CachorroCorredor("Rex")
cachorro.fazer_som()  # Rex fazendo som
cachorro.amamentar()  # Rex amamentando
cachorro.latir()  # Rex faz au au!
cachorro.correr(10)  # Rex correndo a 10 km/h
