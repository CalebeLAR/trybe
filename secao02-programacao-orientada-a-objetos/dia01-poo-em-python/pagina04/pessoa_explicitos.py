def método(self, idade: int) -> None:
    print(f"{self.nome} tem {idade} anos.")


def diz_bom_dia(self) -> None:
    print(f"{self.name} deu bom dia")


class Pessoa:
    diz_nome_e_idade = método
    diz_bom_dia = diz_bom_dia


maria = Pessoa()
maria.nome = "Maria"
maria.diz_nome_e_idade(20)  # saída: Maria tem 20 anos.
