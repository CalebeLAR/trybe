from heranca import Liquidificador


class Pessoa:
    def __init__(self, nome: str, saldo_na_conta: float) -> None:
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador: Liquidificador | None = None

    def comprar_liquidificador(self, liquidificador: Liquidificador) -> None:
        if liquidificador.preço <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preço
            self.liquidificador = liquidificador
