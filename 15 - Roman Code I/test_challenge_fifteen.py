import pytest
from roman_numeral import roman_to_int
@pytest.mark.fifteen
def test_1():
    assert roman_to_int('XLVII') == 47

@pytest.mark.fifteen
def test_2():
    assert roman_to_int('CDXXXVIII') == 438

@pytest.mark.fifteen
def test_3():
    assert roman_to_int('CMIX') == 909

@pytest.mark.fifteen
def test_4():
    assert roman_to_int('MMMCMXCIX') == 3999
