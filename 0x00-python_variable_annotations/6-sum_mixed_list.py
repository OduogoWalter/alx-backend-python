#!/usr/bin/env python3
"""
This module contains a type-annotated function
for summing a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and
    returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list
        containing integers and floats.

    Returns:
        float: The sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)
