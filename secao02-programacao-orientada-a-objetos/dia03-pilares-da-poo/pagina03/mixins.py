class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class MixinVoar:
    def voar(self):
        print("Pássaro voando...")


class Passaro(Animal, MixinVoar):
    def __init__(self, name: str) -> None:
        super().__init__(name)


passaro = Passaro("Pardal")
passaro.voar()  # Pássaro voando...
