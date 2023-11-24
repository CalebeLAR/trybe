class Node:
    def __init__(self, value):
        self.value = value  # 🎲 Dado a ser armazenado
        self.next = None  # 👉 Forma de apontar para outro nó

    def __str__(self):
        return f"Node(value={self.value}, next={self.next})"


if __name__ == "__main__":
    # Este código será executado apenas se meu_modulo.py for executado
    # diretamente, não quando for importado por outro módulo

    node1 = Node("node1_instance")
    node2 = Node("node2_instance")
    node1.next = node2

    print(node1)
