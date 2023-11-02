from typing import Any


class Pai:
    def faz_algo(self, valor: Any) -> None:
        print(valor)


class Filha(Pai):
    def faz_outra_coisa(self) -> None:
        print("Método da classe Pai")

        # Chama o método da superclasse `Pai` passando o `self`
        # explicitamente
        Pai.faz_algo(self, valor=1)


sub_objeto = Filha()
sub_objeto.faz_outra_coisa()
# Método da classe Pai
# 1
