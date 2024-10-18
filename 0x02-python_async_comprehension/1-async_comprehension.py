#!/usr/bin/env python3
"""
An async_comprehension function module.
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns a list of yielded values from a generator.
    """
    myList = [i async for i in async_generator()]
    return myList
