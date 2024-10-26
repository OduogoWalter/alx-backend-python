#!/usr/bin/env python3
"""
This module contains a type-annotated function
that zooms into an array by repeating each element.
"""

from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Takes a list of integers and repeats each element
    in the list by the given factor.

    Args:
        lst (List[int]): A list of integers.
        factor (int): The repetition factor (default is 2).

    Returns:
        List[int]: A list where each element is
        repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
