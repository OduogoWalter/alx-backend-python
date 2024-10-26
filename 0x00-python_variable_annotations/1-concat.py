#!/usr/bin/env python3
"""
This module defines a type-annotated function for concatenating two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The fisrt string.
        str2 (str): The second string.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return str1 + str2
