#!/usr/bin/env python3
"""
A wait_n function module.
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays
    (float values) in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    lst = []
    for task in asyncio.as_completed(tasks):
        lst.append(await task)
    return lst
