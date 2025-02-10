"""
Calculator class for performing and managing arithmetic calculations.
"""

from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from calculator.calculations import Calculations

class Calculator:
    """Performs and stores arithmetic calculations."""

    @staticmethod
    def _execute(x: Decimal, y: Decimal, operation:
                 Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Creates and executes a calculation, storing it in history."""
        calculation = Calculation(x, y, operation)
        Calculations.add(calculation)
        return calculation.result

    @staticmethod
    def add(x: Decimal, y: Decimal) -> Decimal:
        """Performs addition and stores the result."""
        return Calculator._execute(x, y, add)

    @staticmethod
    def subtract(x: Decimal, y: Decimal) -> Decimal:
        """Performs subtraction and stores the result."""
        return Calculator._execute(x, y, subtract)

    @staticmethod
    def multiply(x: Decimal, y: Decimal) -> Decimal:
        """Performs multiplication and stores the result."""
        return Calculator._execute(x, y, multiply)

    @staticmethod
    def divide(x: Decimal, y: Decimal) -> Decimal:
        """Performs division and stores the result."""
        return Calculator._execute(x, y, divide)

    @staticmethod
    def get_history():
        """Retrieves the full history of calculations."""
        return Calculations.get_all()

    @staticmethod
    def get_latest():
        """Retrieves the latest calculation result."""
        return Calculations.get_latest()

    @staticmethod
    def clear_history():
        """Clears the calculation history."""
        Calculations.clear()
