#!/usr/bin/env python3
"""
A measure_runtime function module.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Returns the total runtime for executing
    async_comprehension function four times.
    """
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    total_runtime = time.perf_counter() - start
    return total_runtime
