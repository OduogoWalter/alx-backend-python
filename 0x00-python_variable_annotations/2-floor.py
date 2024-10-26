#!/usr/bin/env python3
"""
This module defines a type-annotated function
for calculating the floor af a float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the floating-point number n.

    Args:
        n (float): The float number to find the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
