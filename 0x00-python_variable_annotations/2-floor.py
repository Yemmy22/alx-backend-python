#!/usr/bin/env python3
"""
A floor function module.
"""


def floor(n: float) -> int:
    """
    Returns a floor value of the input parameter
    """
    a, b = str(n).split('.')

    if int(b[0]) >= 5:
        n = int(a) + 1
    else:
        n = int(a)

    return n
