import pytest
from inverted_array import inverted_array

@pytest.mark.three
def test_1():
    res = inverted_array([0,9,6,8,9,1,5,7])
    assert res == [7,5,1,9,8,6,9,0]

@pytest.mark.three
def test_2():
    res = inverted_array(['Oh', "Hi", "Mark"])
    assert res == ["Mark", "Hi", "Oh"]

@pytest.mark.three
def test_3():
    res = inverted_array([False, True, True, True])
    assert res == [True, True, True, False]

@pytest.mark.three
def test_4():
    res = inverted_array(["It's", "not", True, 0])
    assert res == [0, True, "not", "It's"]

@pytest.mark.three
def test_5():
    pass