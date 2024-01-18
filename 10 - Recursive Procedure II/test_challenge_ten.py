import pytest
from factorial import factorial

@pytest.mark.ten
def test_1():
    assert factorial(5) == 120

@pytest.mark.ten
def test_2():
    assert factorial(0) == 1

@pytest.mark.ten
def test_3():
    assert factorial(32) == 263130836933693530167218012160000000

@pytest.mark.ten
def test_4():
    assert factorial(9) == 362880
