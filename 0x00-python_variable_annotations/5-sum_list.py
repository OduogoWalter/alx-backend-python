#!/usr/bin/env python3
"""
This module contains a type-annotated function for summing a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats in the input_list.
    """
    return sum(input_list)
