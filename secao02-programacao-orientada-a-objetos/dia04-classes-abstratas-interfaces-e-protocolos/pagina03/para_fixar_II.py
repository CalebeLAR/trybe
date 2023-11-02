# Para fixar
# Exercício 2

# Crie uma interface informal em Python chamada Produto, ela deve definir um
# método abstrato chamado imprimir_preco. Caso o método imprimir_preco não
# seja implementado, lance uma exceção NotImplementedError. Crie também uma
# subclasse Livro, que será o nosso exemplo de Produto nesse exercício e
# implemente o método imprimir_preco para mostrar o preço do livro na tela.


class Produto:
    # interface informal
    def imprimir_preco():
        raise NotImplementedError(
            "Classes derivadas de Funcionario precisam implementar"
            + " o imprimir_preco."
        )


class Livro(Produto):
    # classe que deriva da interface informal
    def imprimir_preco(self):
        print("livro custa tantos R$")


if __name__ == "__main__":
    livro = Livro()
    livro.imprimir_preco()
