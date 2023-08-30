from abc import ABC, abstractmethod

# Vamos praticar?
# Exercício 1

# Você trabalha em uma empresa que desenvolve sistemas de gestão para empresas
# de diversos segmentos. Então, o seu gerente de projetos pediu a você que
# desenvolvesse uma classe abstrata chamada Funcionario que servirá de base
# para as classes Programador, Analista e Gerente. Nessa classe abstrata
# deverá conter um método abstrato chamado calcularBonificacao a ser
# implementado nas classes filhas. Então, o método calcularBonificacao deverá
# retornar o valor do salário do funcionário acrescido de um bônus, que
# precisa ser calculado da seguinte forma:

#     Para o Programador o bônus será de 20% do salário;
#     Para o Analista o bônus será de 30% do salário;
#     Para o Gerente o bônus será de 40% do salário;
#     Para as demais funções o bônus será de 10% do salário.

# Crie uma classe chamada Main com um método main que instancie um objeto de
# cada uma das classes filhas. Além disso, ele devem imprimir o valor do
# salário e da bonificação de cada um deles.

# Formate a saída dos valores numéricos para que sejam impressos com duas
# casas decimais.


class Funcionario(ABC):
    @abstractmethod
    def calcularBonificacao(self) -> str:
        pass


class Programador(Funcionario):
    def __init__(self, salario: float) -> None:
        self.salario = salario

    def calcularBonificacao(self) -> str:
        return f"bonificação é de: {'{:.2f}'.format(self.salario * 1.20)}"


class Analista(Funcionario):
    def __init__(self, salario: float) -> None:
        self.salario = salario

    def calcularBonificacao(self) -> str:
        return f"bonificação é de: {'{:.2f}'.format(self.salario * 1.30)}"


class Gerente(Funcionario):
    def __init__(self, salario: float) -> None:
        self.salario = salario

    def calcularBonificacao(self) -> str:
        return f"bonificação é de: {'{:.2f}'.format(self.salario * 1.40)}"


class Colaborador(Funcionario):
    def __init__(self, salario: float) -> None:
        self.salario = salario

    def calcularBonificacao(self) -> str:
        return f"bonificação é de: {'{:.2f}'.format(self.salario * 1.10)}"


class Main:
    def main(self, funcionario: Funcionario) -> None:
        print(funcionario.calcularBonificacao())


if __name__ == "__main__":
    funcionario_geral = Colaborador(1000)
    proramador = Programador(2000)
    analista = Analista(3000)
    gerente = Gerente(4000)

    Main().main(funcionario_geral)
    Main().main(proramador)
    Main().main(analista)
    Main().main(gerente)
