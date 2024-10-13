#!/usr/bin/env python3
"""
An element_length function module.
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element and its length
    """
    return [(i, len(i)) for i in lst]
