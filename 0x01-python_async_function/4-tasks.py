#!/usr/bin/env python3
"""
A task_wait_n function module.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Modifies wait_n function by calling task_wait_random
    function for task creation.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    lst = []
    for task in asyncio.as_completed(tasks):
        lst.append(await task)
    return lst
