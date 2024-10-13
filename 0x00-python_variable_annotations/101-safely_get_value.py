#!/usr/bin/env python3
"""
A safely_get_value function module.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Returns the value of the dict key or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
