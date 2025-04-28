#!/usr/bin/env python3
"""Main file to test task_wait_random function."""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    """Test async function to verify the type of the task."""
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


asyncio.run(test(5))
