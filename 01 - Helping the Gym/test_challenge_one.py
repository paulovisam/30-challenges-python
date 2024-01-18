from arithmetic_average import arithmetic_average
import pytest

@pytest.mark.one
def test_1():
    values = [10, 9, 6, 8, 9, 1, 5, 7]
    expected = 6.875
    result = arithmetic_average(values)
    assert expected == result

@pytest.mark.one
def test_2():
    values = [2, 5, 7, 1, -2]
    expected = 2.6
    result = arithmetic_average(values)
    assert expected == result

@pytest.mark.one
def test_3():
    values = [10, 10, 10, 10, 9]
    expected = 9.8
    result = arithmetic_average(values)
    assert expected == result

@pytest.mark.one
def test_4():
    values = [25, 75]
    expected = 50
    result = arithmetic_average(values)
    assert expected == result
