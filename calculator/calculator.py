"""
Refactored Calculator Module using OOP.
"""

from calculator.calculation import Calculation

class Calculator:
    """Performs calculations using Calculation class."""
    @staticmethod
    def perform_operation(x: float, y: float, operation):
        """
        Creates a Calculation object and returns the result.
        """
        calculation = Calculation(x, y, operation)
        return calculation.get_result()
