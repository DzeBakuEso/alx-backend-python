#!/usr/bin/env python3
"""Module to create an asyncio Task from wait_random coroutine."""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio Task for wait_random.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: A Task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
