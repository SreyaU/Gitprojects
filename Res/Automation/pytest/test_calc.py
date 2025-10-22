import pytest
from calc import add

def test_add_positive():
    assert add(2, 3) == 6

def test_add_negative():
    assert add(-1, -2) == -3

def test_add_mixed():
    assert add(-1, 5) == 4
