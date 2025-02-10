"""
Unit tests for the basic calculator module.
"""

import pytest
from calculator.calculator import add, subtract, multiply, divide

def test_add():
    """Tests the add function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtract function."""
    assert subtract(5, 2) == 3

def test_multiply():
    """Tests the multiply function."""
    assert multiply(3, 4) == 12

def test_divide():
    """Tests the divide function."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Tests division by zero, expecting an exception."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)
