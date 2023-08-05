class Conjunto:
    def __init__(self):
        self.vetor = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.vetor[item]:
            self.vetor[item] = True
            # saber qual é o ultimo elemento que entrou
            # o maior
        if item > self.last_element:
            self.last_element = item

    def __str__(self):
        string = "{"

        for index, is_in_vetor in enumerate(self.vetor):
            if is_in_vetor:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string

    def __contains__(self, item):
        return self.vetor[item]

    def union(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.vetor[index] or conjunto_b.vetor[index]:
                new_conjunto.add(index)

        return new_conjunto

    def intersection(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.vetor[index] and conjunto_b.vetor[index]:
                new_conjunto.add(index)

        return new_conjunto


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
