import pytest
from is_amount_letter import is_amount_letter

@pytest.mark.nine
def test_1():
    res = is_amount_letter('This is Thee')
    assert res == True

@pytest.mark.nine
def test_2():
    res = is_amount_letter('ssd')
    assert res == False

@pytest.mark.nine
def test_3():
    res = is_amount_letter('Lorem ipsum')
    assert res == False

@pytest.mark.nine
def test_4():
    res = is_amount_letter('QQwweerrttyy')
    assert res == True
