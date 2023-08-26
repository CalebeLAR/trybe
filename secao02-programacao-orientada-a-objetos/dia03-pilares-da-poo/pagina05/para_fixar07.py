# Exercício 7

# Crie uma classe GastoMensal que contenha os seguintes atributos:
#   internet: público
#   supermercado: público
#   luz: protegido
#   agua:protegido
#   aluguel: privado


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

