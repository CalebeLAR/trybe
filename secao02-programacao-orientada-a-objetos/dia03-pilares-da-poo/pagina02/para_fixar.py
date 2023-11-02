# Exercício 1
# Crie uma classe chamada Vehicle, que possui um atributo name do tipo string,
# capacity do tipo inteiro e um método move, que recebe um parâmetro distance
# do tipo inteiro e que retorna a mensagem '{self.name} carried {self.capacity}
# people across {distance} kilometers.'. Crie uma classe Car que herda de
# Vehicle e modifica o método move para indicar, no começo da frase já
# existente, que foi especificamente um carro que levou as pessoas. Crie uma
# classe Motorcycle que herda de Vehicle e que tem capacidade fixada em 2.


class Vehicle:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

    def move(self, distance: int) -> str:
        return (
            f"{self.name} carried {self.capacity} people across "
            f"{distance} kilometers."
        )


class Car(Vehicle):
    def __init__(self, capacity: int):
        super().__init__("Carro", capacity)

    def move(self, distance: int) -> str:
        return "a " + super().move(distance)


class Motorcycle(Vehicle):
    def __init__(self) -> None:
        super().__init__("Motorcycle", 2)

    def move(self, distance: int) -> str:
        return "a " + super().move(distance)


print(Car(50).move(50))
print(Motorcycle().move(50))


# Exercício 2

# Crie uma classe chamada Contact (contato), que deverá ter os atributos name
# e email. Crie uma classe chamada ContactList que deverá ter os atributos do
# tipo lista contacts e favorites. Esta classe deverá ter os métodos:

#     * add_contact: recebe um contato e o adiciona na lista
#     * remove_contact: recebe um nome e o remove da lista, retornando-o
#     * add_to_favorites: recebe um nome e o move da lista de contatos para a
#       de favoritos
#     * remove_from_favorites: recebe um nome e o move da lista de favoritos
#     para a de contatos

# Os três últimos métodos devem levantar um LookupError no caso do contato não
# ser encontrado.


class Contact:
    def __init__(self, email: str, name: str):
        self.name = name
        self.email = email


class ContactList(Contact):
    def __init__(self, email: str, name: str) -> None:
        super().__init__(email, name)
        self.contactList: list[Contact] = []
        self.favorites: list[Contact] = []

    def __str__(self) -> str:
        return f"ContactList({self.email})"

    def add_contact(self, contact: Contact) -> None:
        # add_contact: recebe um contato e o adiciona na lista
        if not isinstance(contact, Contact):
            raise ValueError("passe um nome do tipo str")

        if not isinstance(contact, Contact):
            raise ValueError("passe um objeto do tivo Contact")

        self.contactList.append(contact)

    def remove_contact(self, nome: str) -> Contact:
        # remove_contact: recebe um nome e o remove da lista, retornando-o
        if not isinstance(nome, str):
            raise ValueError("passe um nome do tipo str")

        for contact in self.contactList:
            if contact.name == nome:
                self.contactList.remove(contact)
                return contact

        raise LookupError("contanto não encontrado")

    def add_to_favorites(self, nome: str) -> None:
        # add_to_favorites: recebe um nome e o move da lista de contatos para a
        # list de favoritos
        if not isinstance(nome, str):
            raise ValueError("passe um nome do tipo str")

        for contact in self.contactList:
            if contact.name == nome:
                self.contactList.remove(contact)
                self.favorites.append(contact)

        raise LookupError("contanto não encontrado")

    def remove_from_favorites(self, nome: str) -> None:
        # remove_from_favorites: recebe um nome e o move da lista de favoritos
        # para a de contatos
        if not isinstance(nome, str):
            raise ValueError("passe um nome do tipo str")

        for contact in self.contactList:
            if contact.name == nome:
                self.contactList.remove(contact)
                self.favorites.append(contact)

        raise LookupError("contanto não encontrado")

