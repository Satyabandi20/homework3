"""
Unit tests for the Advanced Calculator.
"""

import pytest
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations

@pytest.fixture(autouse=True)
def setup():
    """Clears history before each test to ensure clean state."""
    Calculations.clear()

@pytest.mark.parametrize("x, y, operation, expected", [
    (3, 2, add, 5),
    (10, 5, subtract, 5),
    (4, 3, multiply, 12),
    (20, 4, divide, 5),
])
def test_operations(x, y, operation, expected):
    """Tests basic arithmetic operations."""
    result = Calculator._execute(Decimal(x), Decimal(y), operation)
    assert result == expected

def test_calculator_history():
    """Tests calculation history storage and retrieval."""
    Calculator.add(Decimal(2), Decimal(2))
    Calculator.subtract(Decimal(5), Decimal(3))

    assert len(Calculations.get_all()) == 2
    assert Calculations.get_latest().result == Decimal(2)

def test_clear_history():
    """Tests clearing the history."""
    Calculator.multiply(Decimal(3), Decimal(3))
    assert len(Calculations.get_all()) == 1
    Calculator.clear_history()
    assert len(Calculations.get_all()) == 0

def test_divide_by_zero():
    """Tests division by zero handling."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(Decimal(10), Decimal(0))

def test_clear_history():
    """Tests clearing the calculation history."""
    Calculator.add(Decimal(2), Decimal(2))
    assert len(Calculations.get_all()) == 1
    Calculator.clear_history()
    assert len(Calculations.get_all()) == 0

def test_get_latest_calculation():
    """Tests retrieving the latest calculation."""
    Calculator.subtract(Decimal(10), Decimal(2))
    latest_calc = Calculator.get_latest()
    assert latest_calc.result == Decimal(8)

def test_find_by_operation():
    """Tests finding calculations by operation type."""
    Calculator.multiply(Decimal(5), Decimal(2))
    Calculator.multiply(Decimal(3), Decimal(3))
    
    results = Calculations.find_by_operation("multiply")
    assert len(results) == 2
    assert results[0].result == Decimal(10)
    assert results[1].result == Decimal(9)
