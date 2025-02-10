"""
Manages a history of past calculations.
"""

from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Manages storage and retrieval of previous calculations.""" 
    _history: List[Calculation] = []

    @classmethod
    def add(cls, calculation: Calculation):
        """Adds a calculation to history."""
        cls._history.append(calculation)

    @classmethod
    def get_all(cls) -> List[Calculation]:
        """Returns all stored calculations."""
        return cls._history

    @classmethod
    def clear(cls):
        """Clears all stored calculations."""
        cls._history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieves the most recent calculation."""
        return cls._history[-1] if cls._history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Finds all calculations of a specific operation type."""
        return [calc for calc in cls._history if calc.operation.__name__ == operation_name]
