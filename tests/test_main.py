import pytest
import main as mn




def test_addition():
    result = mn.addition(2, 3)
    assert result == 5


def test_subtraction():
    result = mn.subtraction(5.5, 3)
    assert result == 2.4
