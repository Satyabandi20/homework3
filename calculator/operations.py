"""
Module defining basic arithmetic operations.
"""

def add(x: float, y: float) -> float:
    """Returns the sum of two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Returns the difference of two numbers."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Returns the product of two numbers."""
    return x * y

def divide(x: float, y: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError if division by zero occurs."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
