#!/usr/bin/env python3
"""
Measure the total runtime of running async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel using asyncio.gather,
    and measures the total runtime.

    Returns:
        float: Total time taken to execute all 4 comprehensions.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
