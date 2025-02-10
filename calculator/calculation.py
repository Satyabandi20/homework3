"""
Module defining a Calculation class to encapsulate arithmetic operations.
"""

from typing import Callable

class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, x: float, y: float, operation: Callable[[float, float], float]):
        """Initializes the calculation with operands and an operation."""
        self.x = x
        self.y = y
        self.operation = operation
        self.result = self.operation(x, y)

    def get_result(self) -> float:
        """Returns the result of the calculation."""
        return self.result
