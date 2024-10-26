#!/usr/bin/env python3
"""
This module contains a duck-typed
function to get the first element of a sequence safely.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence and returns its first
    element if available, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of any type.

    Returns:
        Union[Any, None]: The first element
        of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
