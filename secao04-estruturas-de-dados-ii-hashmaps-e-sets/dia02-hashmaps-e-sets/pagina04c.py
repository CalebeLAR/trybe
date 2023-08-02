class Conjunto:
    def __init__(self):
        self.vetor = [False for i in range(1001)]

    def add(self, item):
        if 0 <= item <= 1000:
            self.vetor[item] = True

    def __str__(self):
        # retorno: uma string que representa o seu objeto
        str = ""
        for i, e in enumerate(self.vetor):
            if e is True:
                str += f"{i}, "

        return "{" + f"{str[0:-2]}" + "}"

    def __contains__(self, item):
        # retorno: True, caso o elemento faça parte. False, caso o elemento
        # não faça parte.
        return self.vetor[item]

    def union(self, conjunto_b):
        # retorno: outro objeto Conjunto com união do próprio objeto com o
        # conjunto_b
        for i, e in enumerate(conjunto_b.vetor):
            if e is True:
                self.vetor[i] = e

        return self.vetor

    def intersection(self, conjunto_b):
        # retorno: outro objeto Conjunto com intersecção do próprio objeto
        # com o conjunto_b
        new = Conjunto()
        for i, e in enumerate(conjunto_b.vetor):
            if e is True and self.vetor[i] is True:
                new.add(i)

        return new


if __name__ == "__main__":
    conjunto = Conjunto()

    for item in [0, 10, 100, 1000]:
        conjunto.add(item)
    A = [ele for ele in conjunto.vetor]
    print(conjunto)

    print("# retorno: outro objeto Conjunto com união", end="")
    print("do próprio objeto com o conjunto_b")

    conjunto_b = Conjunto()
    for item in [1, 10, 100, 11, 101, 991]:
        conjunto_b.add(item)
    B = [ele for ele in conjunto_b.vetor]

    print(conjunto)
    print(conjunto_b)

    print(conjunto.intersection(conjunto_b))
    print(conjunto_b.intersection(conjunto))
