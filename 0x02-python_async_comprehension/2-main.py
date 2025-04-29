#!/usr/bin/env python3

import asyncio

# Import the measure_runtime coroutine from the '2-measure_runtime.py' file
measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await measure_runtime()  # Fixed the syntax error here

# Run the main function and print the total runtime
print(asyncio.run(main()))
