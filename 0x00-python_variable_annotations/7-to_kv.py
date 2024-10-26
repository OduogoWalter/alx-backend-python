#!/usr/bin/env python3
"""
This module contains a type-annotated function
that returns a tuple of astring and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number (int or float) and returns a tuple.
    The first element of the tuple is the string.
    The second element is the square of the number, and it is a float.

    Args:
        k (str): A string value.
        v (Union[int, float]): A number (int or float).

    Returns:
        Tuple[str, float]: A tuple where the
        first element is the string k and
        the second element is the square of v as a float.
    """
    return (k, float(v ** 2))
