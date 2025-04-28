#!/usr/bin/env python3
"""Module that defines an async routine to run multiple coroutines concurrently."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns a list of all the delays (float values) in ascending order without using sort().

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
