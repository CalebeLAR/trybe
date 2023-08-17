# main.py
def mean(numbers):
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


# minha função para testar o @pytest.mark.parametrize
def are_all_numbers_even(numbers):
    # doctests
    for num in numbers:
        if num % 2 == 0:
            return False
            break

    return True
