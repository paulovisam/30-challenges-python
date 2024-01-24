import pytest
from caesar_cipher import decript_cipher
@pytest.mark.sixteen
def test_1():
    assert decript_cipher('Vguvg',2) == "Teste"

@pytest.mark.sixteen
def test_2():
    assert decript_cipher('BCDYZAbcdyza', 27) == 'ABCXYZabcxyz'

@pytest.mark.sixteen
def test_3():
    assert decript_cipher('Qaiik', 60) == "Isaac"

@pytest.mark.sixteen
def test_4():
    assert decript_cipher('Amozmlw', 8) == 'Segredo'
