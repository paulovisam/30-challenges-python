from recurse import chunk
import pytest

@pytest.mark.two
def test_1():
    res = chunk(4)
    assert res == "chunk-chunk-chunk-chunk"

@pytest.mark.two
def test_2():
    res = chunk(1)
    assert res == "chunk"

@pytest.mark.two
def test_3():
    res = chunk(8)
    assert res == "chunk-chunk-chunk-chunk-chunk-chunk-chunk-chunk"

@pytest.mark.two
def test_4():
    res = chunk(2)
    assert res == "chunk-chunk"