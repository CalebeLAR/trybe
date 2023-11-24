from pagina04c_gab import Conjunto


def test_testa_se_dá_de_criar_uma_instancia_de_Conjunto():
    """testa se dá de criar uma instancia de Conjunto"""
    conjunto = Conjunto()

    assert isinstance(conjunto, Conjunto)
    assert conjunto.vetor == [False for i in range(1001)]


def test_testa_a_implementação_do_metodo_add():
    """testa a implementação do metodo add"""
    conjunto = Conjunto()
    conjunto.add(0)
    assert conjunto.vetor[0] is not False

    conjunto.add(1)
    assert conjunto.vetor[1] is True
    assert conjunto.vetor[0] is not False

    head = [True, True]
    tail = [False for i in range(2, 1001)]
    head.extend(tail)

    assert conjunto.vetor == head


def test_testa_a_implementação_do_metodo__str__(capfd):
    """testa a implementação do metodo __str__"""
    conjunto = Conjunto()

    for num in [0, 10, 100, 1000]:
        conjunto.add(num)

    print(conjunto)
    out, err = capfd.readouterr()
    assert out.strip() == "{0, 10, 100, 1000}"


def test_testa_a_implementação_do_metodo__contain__():
    """testa a implementação do metodo __contain__"""
    conjunto = Conjunto()

    for num in [0, 10, 100, 1000]:
        conjunto.add(num)

    assert (10 in conjunto) is True
    assert (11 in conjunto) is False


def test_testa_a_implementação_do_metodo__union__():
    """testa a implementação do metodo __union__"""
    conjuntoA = Conjunto()
    conjuntoB = Conjunto()

    for num in range(1001):
        if num % 2 == 0:
            conjuntoA.add(num)
        else:
            conjuntoB.add(num)


def test_testa_a_implementação_do_metodo__intersection__(capfd):
    """testa a implementação do metodo __intersection__"""
    conjuntoA = Conjunto()
    conjuntoB = Conjunto()

    for item in [0, 10, 100, 991, 1000]:
        conjuntoA.add(item)

    for item in [1, 10, 100, 11, 101, 991]:
        conjuntoB.add(item)

    print(conjuntoA.intersection(conjuntoB))
    out, err = capfd.readouterr()
    assert out.strip() == "{10, 100, 991}"

    print(conjuntoB.intersection(conjuntoA))
    out, err = capfd.readouterr()
    assert out.strip() == "{10, 100, 991}"
