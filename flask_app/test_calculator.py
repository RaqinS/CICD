import pytest

from calculator import add,subtract,divide,multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(2, -3) == 5
    assert subtract(0, 0) == 0

def test_divide():
    assert divide(2, 3) == 2/3
    assert divide(-2, 3) == -2/3
    assert divide(2, -3) == 2/-3
    
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-5, -4) == 20
