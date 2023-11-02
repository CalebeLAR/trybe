from abc import ABC, abstractmethod

# Para fixar
# Exercício 1

# Crie uma classe abstrata base chamada Pessoa, que contenha um método abstrato
# chamado imprimir_cargo. Além disso, crie duas subclasses que terão
# implementações concretas da classe base abstrata.
# São elas: Vendedor e Gerente. O método imprimir_cargo deverá imprimir
# “Meu cargo é de vendedor” e “Meu cargo é de gerente” respectivamente.


class Pessoa(ABC):
    @abstractmethod
    def imprimir_cargo(self):
        pass


class Vendedor(Pessoa):
    def imprimir_cargo(self):
        print('Meu cargo é de Vendedor')


class Gerente(Pessoa):
    def imprimir_cargo(self):
        print('Meu cargo é de gerente')
    pass


if __name__ == '__main__':
    vendedor = Vendedor()
    vendedor.imprimir_cargo()

    gerente = Gerente()
    gerente.imprimir_cargo()
