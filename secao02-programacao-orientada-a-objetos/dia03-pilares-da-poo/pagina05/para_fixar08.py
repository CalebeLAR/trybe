# Exercício 8

# Utilize o código que você criou no exercício anterior e crie os métodos
# get e set para os atributos luz e agua.


class GastoMensal:
    def __init__(
        self,
        internet: float,
        supermercado: float,
        luz: float,
        agua: float,
        aluguel: float,
    ) -> None:
        self.internet = internet
        self.supermercado = supermercado
        self._luz = luz
        self._agua = agua
        self.__aluguel = aluguel

    @property
    def luz(self) -> int:
        return self._luz

    @luz.setter
    def luz(self, value: int) -> int:
        self._luz = value

    @property
    def agua(self) -> int:
        return self._agua

    @agua.setter
    def agua(self, value: int) -> int:
        self._agua = value


if __name__ == "__main__":
    april = GastoMensal(100, 100, 100, 100, 100)
    print(april.luz)
    print(april.agua)
    april.luz = 120
    april.agua = 120
    print(april.luz)
    print(april.agua)
