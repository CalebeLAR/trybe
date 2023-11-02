#  Exercício 3

# Crie uma classe Animal com um atributo nome e um método fazer_som
# que imprime “Animal fazendo som”. Depois, crie uma classe Mamifero
# que herda de Animal e tenha um método amamentar. Por fim, crie uma
# classe Cachorro que herda de Mamifero e tenha um método latir e
# imprima “Au au!”.


class Animal:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def fazer_som(self) -> None:
        print("Animal fazendo som")


class Mamifero(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def amamentar(self):
        print(f"{self.nome} está amamentando")


class Cachorro(Mamifero):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def latir(self) -> None:
        super().fazer_som()
        print("AU AU AU")


if __name__ == '__main__':
    cachorro = Cachorro('chapel')
    cachorro.latir()

# Exercício 4

# Utilize a sua solução do exercício anterior e faça um mixin que conterá um
# método para mostrar a velocidade que o cachorro está correndo.
