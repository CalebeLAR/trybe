from Liquidificador import Liquidificador


class Pessoa:
    def __init__(self, nome: str, idade=None, saldo_na_conta=None) -> None:
        self.idade = idade
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador: Liquidificador | None = None

    def comprar_liquidificador(self, liquidificador: Liquidificador) -> None:
        if liquidificador.preço <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preço
            self.liquidificador = liquidificador


liqui_rosa = Liquidificador("rosa", 12, 8, 120.00)
pessoa = Pessoa("larissa manueda", 10)
pessoa_1 = Pessoa("Marcelo", 22, 700)
pessoa_2 = Pessoa("Matheus")
pessoa_3 = Pessoa("Maria", 33)
pessoa_4 = Pessoa("Márcia", saldo_na_conta=100)
