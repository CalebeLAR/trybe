# Exercício 10
# Agora, crie uma função imprimir_detalhes para mostrar na tela informações
# sobre os seguintes produtos:
from para_fixar09 import Livro, DVD, Produto


def imprimir_detalhes(produto: Produto):
    print(f"Descrição: {produto.descrever()}")
    print(f"Preço: {produto.preço()}")


produtos = [
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 29.99),
    DVD("O Poderoso Chefão", "Francis Ford Coppola", 19.99),
]

for produto in produtos:
    imprimir_detalhes(produto)

# Saída:
# Descrição: O Senhor dos Anéis por J.R.R. Tolkien
# Preço: 29.99
# Descrição: O Poderoso Chefão dirigido por Francis Ford Coppola
# Preço: 19.99
