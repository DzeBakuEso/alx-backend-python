#!/usr/bin/env python3
"""
Module that defines an asynchronous generator
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers between 0 and 10 asynchronously
    after a 1-second wait for each iteration.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
