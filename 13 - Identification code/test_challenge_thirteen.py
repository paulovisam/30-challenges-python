import pytest
from is_valid_code import is_valid_code

@pytest.mark.thirteen
def test_1():
    assert is_valid_code(547020743789)

@pytest.mark.thirteen
def test_2():
    assert is_valid_code(301354030348)
@pytest.mark.thirteen
def test_3():
    assert not is_valid_code(301354030349)

@pytest.mark.thirteen
def test_4():
    assert not is_valid_code(123456789872)
