#!/usr/bin/env python3
"""
A sum_mixed_list function module.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of parameter list elements
    """
    res = 0

    for element in mxd_lst:
        res += element

    return res
