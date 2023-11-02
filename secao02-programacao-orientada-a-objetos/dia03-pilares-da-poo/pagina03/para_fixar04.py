# Exercício 4

# Utilize a sua solução do exercício anterior e faça um mixin que conterá um
# método para mostrar a velocidade que o cachorro está correndo.
from para_fixar03 import Mamifero


class MixinVelocidade:
    def __init__(self, velocidade: str) -> None:
        self.velocidade = velocidade

    def ver_velocidade(self) -> None:
        print(f"{self.velocidade}")


class Cachorro(Mamifero, MixinVelocidade):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def latir(self) -> None:
        super().fazer_som()
        print("AU AU AU")


if __name__ == "__main__":
    cachorro = Cachorro("chapel")
    cachorro.latir()
    cachorro.velocidade = "33km/h"
    cachorro.ver_velocidade()
