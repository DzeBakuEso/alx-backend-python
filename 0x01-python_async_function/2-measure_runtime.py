#!/usr/bin/env python3
"""Module to measure the average runtime of an async routine."""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n and returns the average time per task.

    Args:
        n (int): Number of times wait_random is spawned.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
