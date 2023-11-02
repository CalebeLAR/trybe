import pytest

from main import mean, are_all_numbers_even


@pytest.mark.parametrize(
    "input_numbers, expected_result",  # 1
    [  # 2
        ([1, 2, 3, 4, 5], 3.0),  # 3
        ([2.5, 3.75, 1.25, 4], 2.875),
    ],
)
def test_mean(input_numbers, expected_result):  # 4
    assert mean(input_numbers) == expected_result


def test_mean_fail():  # 5
    with pytest.raises(ZeroDivisionError):
        mean([])


# teste com o @pytest.mark.parametrize
@pytest.mark.parametrize(
    'input_numbers1, expected_result2',
    [
        ([1, 3, 5, 7, 9], True),
        ([11, 13, 15, 17, 18], False)
    ]
)
def test_are_all_numbers_even(input_numbers1, expected_result2):
    assert are_all_numbers_even(input_numbers1) is expected_result2













# def test_are_all_numbers_even():
#     arr1 = [1, 3, 5, 7, 9]  # true
#     arr2 = [11, 13, 15, 17, 18]  # false

#     assert are_all_numbers_even(arr1) is True
#     assert are_all_numbers_even(arr2) is False
