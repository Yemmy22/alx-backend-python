#!/usr/bin/env python3
"""
An async_generator function module.
"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields a random float value.
    """
    for i in range(10):
        s = uniform(0, 10)
        await asyncio.sleep(1)
        yield s
