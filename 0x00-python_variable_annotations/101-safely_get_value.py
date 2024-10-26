#!/usr/bin/env python3
"""
This module contains a type-annotated
function for safely retrieving values from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from the dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary-like object.
        key (Any): The key to look up.
        default (Union[T, None], optional): The default value
        to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if
        the key is found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
