import pytest


def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_add_fail():
    assert add(1, 2) == 4
