import pytest
from largest_letter import largest_letter

@pytest.mark.five
def test_1():
    res = largest_letter('Lorem ipsum dolore sec avanti')
    assert res == 'v'

@pytest.mark.five
def test_2():
    res = largest_letter('Hello')
    assert res == 'o'

@pytest.mark.five
def test_3():
    res = largest_letter('May the force be with you')
    assert res == 'y'

@pytest.mark.five
def test_4():
    res = largest_letter('Its over nine thousand')
    assert res == 'v'