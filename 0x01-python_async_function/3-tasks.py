#!/usr/bin/env python3
"""
A task_wait_random function module.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns a asyncio.Task object from wait_random
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
