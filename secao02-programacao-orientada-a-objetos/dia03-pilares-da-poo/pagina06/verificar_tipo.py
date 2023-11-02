from Liquidificador import Eletrodoméstico


class Liquidificador(Eletrodoméstico):
    pass


class Ventilador(Eletrodoméstico):
    def __init__(
        self,
        cor: str,
        potencia: str,
        tensao: str,
        preco: str,
        quantidade_de_portas=1,
    ) -> None:
        # Chamada ao construtor da superclasse
        super().__init__(cor, potencia, tensao, preco)

        # Faz outras coisas específicas dessa subclasse
        self.quantidade_de_portas = quantidade_de_portas


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomesticos = []

    # Permite a aquisição de qualquer eletrodoméstico
    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomestico.append(eletrodomestico)
