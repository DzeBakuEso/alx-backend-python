#!/usr/bin/env python3
"""Module that contains an asynchronous coroutine
which waits for a random delay and returns it."""

import asyncio
import random
from typing import Awaitable


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds (inclusive) and returns the delay.
    
    Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.
    
    Returns:
        float: The actual random delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
