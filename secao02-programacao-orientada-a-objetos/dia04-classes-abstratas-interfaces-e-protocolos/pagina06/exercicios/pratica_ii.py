from abc import ABC, abstractmethod

# Exercício 2

# Agora, você deve criar um sistema para gerenciamento de serviços de entrega.
# Para isso, deverá ter uma interface chamada Entregavel que precisa conter um
# método chamado entregar. Essa interface vai ser implementada pelas classes
# Correios e Transportadora. O método entregar deverá receber como parâmetro
# um objeto da classe Cliente e um objeto da classe Endereco. Além disso, o
# método precisa imprimir uma mensagem informando que o serviço foi entregue
# com sucesso.


# ➡️ Siga os passos a seguir para a construção.

#     Crie uma classe chamada Cliente com os atributos nome e telefone.

#     Crie uma classe chamada Endereco com os atributos rua, numero, bairro,
#     cidade e estado.

#     Crie uma classe chamada Correios que implemente a interface Entregavel.

#     Crie uma classe chamada Transportadora que implemente a interface
#     Entregavel.

#     Crie uma classe chamada Main com um método main que instancie um objeto
#     de cada uma das classes Correios e Transportadora. Em seguida, crie um
#     objeto da classe Cliente e um objeto da classe Endereco. Por fim,
#     utilize o método entregar dos objetos Correios e Transportadora passando
#     como parâmetro o objeto Cliente e o objeto Endereco.

#     Lembre-se de usar o mypy para verificar se a tipagem está correta.


class Cliente:
    def __init__(self, nome: str, telefone: str) -> None:
        self.nome = nome
        self.telefone = telefone


class Endereco:
    def __init__(
        self, rua: str, numero: str, bairro: str, cidade: str, estado: str
    ) -> None:
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado


class AbstractEntregavel(ABC):
    @abstractmethod
    def entregar(self, cliente: Cliente, Endereco: Endereco) -> None:
        pass


class Correios(AbstractEntregavel):
    def entregar(self, cliente: Cliente, endereco: Endereco) -> None:
        print(
            "entrega realizada pelos Correios\n"
            "--------------------\n"
            f"Destinatário:    \n"
            f"nome: {cliente.nome}\n"
            "--------------------\n"
            f"telefone: {cliente.telefone}\n"
            f"rua: {endereco.rua}\n"
            f"numero: {endereco.numero}\n"
            f"bairro: {endereco.bairro}\n"
            f"cidade: {endereco.cidade}\n"
            f"estado: {endereco.estado}\n\n\n"
        )


class Transportadora(AbstractEntregavel):
    def entregar(self, cliente: Cliente, endereco: Endereco) -> None:
        print(
            "entrega realizada pelos Correios\n"
            "--------------------\n"
            f"Destinatário:    \n"
            f"nome {cliente.nome}\n"
            "--------------------\n"
            f"telefone: {cliente.telefone}\n"
            f"rua: {endereco.rua}\n"
            f"numero: {endereco.numero}\n"
            f"bairro: {endereco.bairro}\n"
            f"cidade: {endereco.cidade}\n"
            f"estado: {endereco.estado}\n\n\n"
        )


class Main:
    def main(self) -> None:
        cliente = Cliente("carlos", "99 9999-9999")
        endereco = Endereco("tal", "tal", "tal", "tal", "tal")

        correio = Correios()
        transportadora = Transportadora()

        correio.entregar(cliente, endereco)
        transportadora.entregar(cliente, endereco)


if __name__ == "__main__":
    Main().main()
