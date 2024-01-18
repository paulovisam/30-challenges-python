import pytest

import pytest
from inverted_phrase import inverted_phrase

@pytest.mark.six
def test_1():
    res = inverted_phrase('Lorem ipsum dolore sec avanti')
    assert res == 'merol muspi erolod ces itnava'

@pytest.mark.six
def test_2():
    res = inverted_phrase('This is an apple')
    assert res == 'siht si na elppa'

@pytest.mark.six
def test_3():
    res = inverted_phrase('May the force be with you')
    assert res == 'yam eht ecrof eb htiw uoy'

@pytest.mark.six
def test_4():
    res = inverted_phrase('It s over nine thousand')
    assert res == 'ti s revo enin dnasuoht'