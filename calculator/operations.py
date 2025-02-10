"""
Module for basic arithmetic operations.
"""

from decimal import Decimal

def add(x: Decimal, y: Decimal) -> Decimal:
    """Returns the sum of two numbers."""
    return x + y

def subtract(x: Decimal, y: Decimal) -> Decimal:
    """Returns the difference between two numbers."""
    return x - y

def multiply(x: Decimal, y: Decimal) -> Decimal:
    """Returns the product of two numbers."""
    return x * y

def divide(x: Decimal, y: Decimal) -> Decimal:
    """Returns the quotient of two numbers. Raises ValueError if division by zero occurs."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
