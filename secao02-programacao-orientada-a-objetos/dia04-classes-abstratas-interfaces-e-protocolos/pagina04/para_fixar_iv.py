from para_fixar_iii import CalculaPerimetro

#  Exercício 4

# Quando executamos o mypy no código a seguir, recebemos o erro error: Cannot
# instantiate abstract class "Triangulo" with abstract attribute
# "calcular_perimetro" [abstract]. Corrija-o para que o mypy retorne a
# mensagem de sucesso.


class Triangulo(CalculaPerimetro):
    def __init__(self, lado1: int, lado2: int, lado3: int) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self) -> str:
        return (
            "O perímetro do triângulo é de"
            + f"{self.lado1 + self.lado2 + self.lado3} cm"
        )


triangulo = Triangulo(5, 5, 5)
print(triangulo.calcular_perimetro())
