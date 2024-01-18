import pytest
from array_merge import array_merge


@pytest.mark.seven
def test_1():
    assert array_merge(
        [[1, 5, 3], [6, 19, 11], [47, 128, 5], [1, 93, 57, 42, 103]]
    ) == [1, 1, 3, 5, 5, 6, 11, 19, 42, 47, 57, 93, 103, 128]


@pytest.mark.seven
def test_2():
    assert array_merge([[1, 3], [4, 8], [7, 5], [2, 6]]) == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.seven
def test_3():
    assert array_merge([[], [], [], []]) == []


@pytest.mark.seven
def test_4():
    assert array_merge([[100, 50], [60, 100], [20, 100, 70], [10, 40, 80, 90]]) == [
        10,
        20,
        40,
        50,
        60,
        70,
        80,
        90,
        100,
        100,
        100,
    ]
