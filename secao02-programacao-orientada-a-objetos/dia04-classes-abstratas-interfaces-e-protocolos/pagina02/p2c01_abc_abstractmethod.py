from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def nome(self):
        pass


class Vendedor(Pessoa):
    def __init__(self, seu_nome):
        self.seu_nome = seu_nome

    def nome(self):
        print(f"Seu nome é: {self.seu_nome}")
