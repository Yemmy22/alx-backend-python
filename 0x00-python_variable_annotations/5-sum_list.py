#!/usr/bin/env python3
"""
A sum_list function module.
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    Returns the sum of parameter list elements
    """
    res = 0

    for element in input_list:
        res += element

    return res
