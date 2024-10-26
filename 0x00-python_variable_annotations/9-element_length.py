#!/usr/bin/env python3
"""
This module contains a type-annotated
function that returns the lengths of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns
    a list of tuples containing each sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., lists, strings, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each
        containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
