import pytest
from raise_to_square import raise_to_square

@pytest.mark.four
def test_1():
    res = raise_to_square(3514)
    assert res == 925116

@pytest.mark.four
def test_2():
    res = raise_to_square(94571)
    assert res == 811625491

@pytest.mark.four
def test_3():
    res = raise_to_square(24)
    assert res == 416

@pytest.mark.four
def test_4():
    res = raise_to_square(745821698)
    assert res == 4916256441368164