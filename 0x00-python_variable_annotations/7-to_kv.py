#!/usr/bin/env python3
"""
A to_kv function module.
"""

from typing import Union, Tuple


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string parameter
    and square of the int/float parameter
    """
    return (k, v**2)
