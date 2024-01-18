import pytest
from abrev import abrev

@pytest.mark.eight
def test_1():
    res = abrev('Isaac Larrubia Ferreira Pontes')
    assert res == 'PONTES, I. L. F.'

@pytest.mark.eight
def test_2():
    res = abrev('John Ronald Reuel Tolkien')
    assert res == 'TOLKIEN, J. R. R.'

@pytest.mark.eight
def test_3():
    res = abrev('christopher james paolini')
    assert res == 'PAOLINI, C. J.'

@pytest.mark.eight
def test_4():
    res = abrev('Suzanne Marie Collins')
    assert res == 'COLLINS, S. M.'