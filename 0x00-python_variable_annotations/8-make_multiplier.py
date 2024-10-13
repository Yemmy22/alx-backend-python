#!/usr/bin/env python3
"""
A make_multiplier function module.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns the return value of a callable
    that squares the parameter input
    """
    def callable(multiplier) -> float:
        return multiplier * multiplier
    return callable
