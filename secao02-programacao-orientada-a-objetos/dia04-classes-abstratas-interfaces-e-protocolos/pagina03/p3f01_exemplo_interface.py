from abc import ABC, abstractmethod


# interfaces
class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self):
        raise NotImplementedError(
            "Classes derivadas de Funcionario precisam implementar"
            + " o cálculo de salário."
        )


class Atendente(Funcionario):
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        super().calcular_salario()


if __name__ == "__main__":
    funcionário = Atendente("maria")
    # funcionário.calcular_salario()
