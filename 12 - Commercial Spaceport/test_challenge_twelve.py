import pytest
from coin_counter import coin_counter


@pytest.mark.twelve
def test_1():
    assert coin_counter(478) == {"1": 3, "5": 0, "10": 0, "25": 3, "100": 4, "500": 0}


@pytest.mark.twelve
def test_2():
    assert coin_counter(384) == {"1": 4, "5": 1, "10": 0, "25": 3, "100": 3, "500": 0}


@pytest.mark.twelve
def test_3():
    assert coin_counter(5412) == {"1": 2, "5": 0, "10": 1, "25": 0, "100": 4, "500": 10}


@pytest.mark.twelve
def test_4():
    assert coin_counter(50) == {"1": 0, "5": 0, "10": 0, "25": 2, "100": 0, "500": 0}
