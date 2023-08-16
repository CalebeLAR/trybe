def mean(numbers):
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean(my_list)
    3.0
    >>> mean([2.5, 3.75, 1.25, 4])
    2.875

    """
    return sum(numbers) / len(numbers)


def mean_first_soluction(numbers):
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean(my_list)
    3.0
    >>> mean([2.5, 3.75, 1.25, 4])
    2.875
    >>> mean([])
    0

    """
    # Adicionamos as duas linhas abaixo. O resto continua igual.
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


def mean_second_soluction(numbers):
    """
    Calcula a média de uma lista de números.

    >>> my_list = [1, 2, 3, 4, 5]
    >>> mean(my_list)
    3.0
    >>> mean([2.5, 3.75, 1.25, 4])
    2.875
    >>> mean([])
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    """
    return sum(numbers) / len(numbers)


def div(a, b):
    """
    >>> div(6, 3)
    2.0
    >>> div(6, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b
