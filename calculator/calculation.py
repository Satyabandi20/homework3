"""
Encapsulates a single arithmetic operation as an object.
"""

from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a single mathematical operation with operands and a function."""    
    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initializes a calculation with two numbers and an operation."""
        self.x = x
        self.y = y
        self.operation = operation
        self.result = self.perform()

    def perform(self) -> Decimal:
        """Executes the operation and returns the result."""
        return self.operation(self.x, self.y)

    def __repr__(self) -> str:
        """String representation of a calculation instance."""
        return f"Calculation({self.x}, {self.y}, {self.operation.__name__})"
