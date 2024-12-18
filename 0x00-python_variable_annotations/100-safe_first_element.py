#!/usr/bin/env python3
"""
A safe_first_element function module.
"""

from typing import Sequence, Any, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the iterable or None.
    """
    if lst:
        return lst[0]
    else:
        return None
