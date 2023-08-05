class Conjunto:
    def __init__(self):
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.set[item]:
            self.set[item] = True
            # saber qual é o ultimo elemento que entrou
            # o maior
        if item > self.last_element:
            self.last_element = item

    def __str__(self):
        string = "{"

        for index, is_in_vetor in enumerate(self.set):
            if is_in_vetor:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string

    def __contains__(self, item):
        return self.set[item]

    def union(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] or conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def intersection(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def difference(self, conjunto_b):
        new_conjunto = Conjunto()
        # A[1,2,3] - B[1,2,5]

        for index, e in enumerate(conjunto_b.set):
            if self.set[index] is True and e is False:
                new_conjunto.add(index)

        return new_conjunto

    def issubset(self, conjunto_b):
        # A[1,2] issubset B[1,2,5]
        # A[1,2] issubset B[A[1,2],5]
        # B[A, 5]

        for index, e in enumerate(conjunto_b.set):
            if self.set[index] is True and e is False:
                return False
                break

        return True

    def issuperset(self, conjunto_b):
        # A[1,2,5,6,7] issubset B[1,2,5]
        # A[B[1,2,5],6,7] issubset B[1,2,5]
        # A[B,6,7] issubset B[1,2,5]
        # true
        for index, e in enumerate(conjunto_b.set):
            if e is True and self.set[index] is False:
                return False
                break
        return True


if __name__ == "__main__":
    conj = Conjunto()
    for i in [0, 10, 100, 1000]:
        conj.add(i)
    print(conj)

    conj2 = Conjunto()
    for i in [1, 2, 3]:
        conj2.add(i)
    print(conj2)

    conj3 = Conjunto()
    for i in [7, 2, 10]:
        conj3.add(i)
    print(conj3)

    conj4 = Conjunto()
    print(conj4)

    conj = Conjunto()
    for i in [1, 2, 3]:
        conj.add(i)
    print(conj)
    print(1 in conj)
    print(0 in conj)

    conj1 = Conjunto()
    for i in range(1, 11):
        conj1.add(i)

    conj2 = Conjunto()
    for i in range(10, 21):
        conj2.add(i)

    conj3 = conj1.union(conj2)
    print(conj3)

    conj1 = Conjunto()
    for i in [1, 2, 3]:
        conj1.add(i)

    conj2 = Conjunto()
    for i in [7, 2, 10]:
        conj2.add(i)

    conj3 = conj1.intersection(conj2)
    print(conj3)

    conj1 = Conjunto()
    for i in [7, 2, 10]:
        conj1.add(i)

    conj2 = Conjunto()
    for i in [7, 3, 1]:
        conj2.add(i)

    conj1 = Conjunto()
    for i in [3, 2]:
        conj1.add(i)

    conj2 = Conjunto()
    for i in [7, 2, 1]:
        conj2.add(i)

    conj1 = Conjunto()
    for i in [1, 2, 3, 4, 5, 6]:
        conj1.add(i)

    conj2 = Conjunto()
    for i in [1, 2, 3]:
        conj2.add(i)

    estudantes = Conjunto()
    for i in [1, 2, 3, 4, 5, 6, 7]:
        estudantes.add(i)

    lista1_entregues = Conjunto()
    for i in [1, 4, 7, 3]:
        lista1_entregues.add(i)

    lista2_entregues = Conjunto()
    for i in [3, 1, 6]:
        lista2_entregues.add(i)

    print("Quem ainda não entregou a lista1?", end="")
    res = estudantes.difference(lista1_entregues)
    print(res)
    print("Quem já entregou as duas listas?", end="")
    res = lista1_entregues.intersection(lista2_entregues)
    print(res)
    print("Quem já entregou qualquer uma das duas listas?", end="")
    res = lista1_entregues.union(lista2_entregues)
    print(res)
    print("Quem ainda não entregou nenhuma das listas?", end="")
    res = estudantes.difference(lista1_entregues).difference(lista2_entregues)
    print(res)
