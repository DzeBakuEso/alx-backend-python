#!/usr/bin/env python3
"""Module to run multiple asyncio Tasks concurrently."""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
