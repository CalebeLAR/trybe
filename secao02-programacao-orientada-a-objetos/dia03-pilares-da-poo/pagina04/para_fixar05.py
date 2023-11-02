# Exercício 5
# Crie uma classe chamada Retangulo que represente um retângulo com os
# atributos base e altura. A classe deve ter métodos para calcular a área e o
# perímetro do retângulo.


class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        self.__pro = 'atest'

    def calc_area(self) -> float:
        return round(self.base * self.altura, 2)

    def calc_perimetro(self) -> float:
        return round(2 * (self.base + self.altura), 2)

    pass
