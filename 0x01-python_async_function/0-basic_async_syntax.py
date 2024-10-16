#!/usr/bin/env python3
"""
A wait_random function module.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns the a floating point ranom value
    from an integer input.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
