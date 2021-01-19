import pytest
import main as mn

def test_addition():
    result = mn.addition(2, 3)
    assert result == 5