from typing import Protocol

# Para fixar
# Exercício 3

# Crie um protocolo chamado CalculaPerimetro que contenha um método abstrato
# chamado calcular_perimetro. Crie uma classe chamada Quadrado que implemente
# o protocolo CalculaPerimetro e o método calcular_perimetro para
# calcular o perímetro do quadrado.


class CalculaPerimetro(Protocol):
    def calcular_perimetro(self) -> str:
        pass


class Quadrado(CalculaPerimetro):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_perimetro(self) -> str:
        return f"O perímetro do quadrado é de {round(4 * self.lado, 2)}cm"


if __name__ == "__main__":
    quadrado = Quadrado(6.5)
    print(quadrado.calcular_perimetro())
