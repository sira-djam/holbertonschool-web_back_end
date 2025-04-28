#!/usr/bin/env python3

"""Module to measure the runtime of async_comprehension."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Measures the total runtime of async_comprehension.

        Returns:
                float: Total runtime in seconds.
        """
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    return end_time - start_time
