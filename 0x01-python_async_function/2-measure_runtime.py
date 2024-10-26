#!/usr/bin/env python3
"""Module for measuring runtime of async functions."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds

    Returns:
        float: Average time per operation
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
