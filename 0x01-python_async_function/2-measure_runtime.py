#!/usr/bin/env python3
"""
A measure_time function module.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """
    Computes and returns the total execution time/n for
    wait_n(n, max_delay).
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end/n
