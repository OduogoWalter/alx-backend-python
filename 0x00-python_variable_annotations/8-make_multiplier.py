#!/usr/bin/env python3
"""
This module contains a type-annotated function
that returns a function to multiply a float.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float 'multiplier' and returns a
    function that multiplies a float by 'multiplier'.

    Args:
        multiplier (float): The multiplier.

    Returns:
        Callable[[float], float]: A function that
        takes a float and returns a float.
    """
    def multiply_by(value: float) -> float:
        """
        Multiplies a float by the given multiplier.
        """
        return value * multiplier

    return multiply_by
