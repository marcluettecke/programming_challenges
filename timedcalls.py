"""
Time a function's processing time by repeatedly calling it
"""

import time


def timed_call(fn, *args):
    """

    Args:
        fn: function to be timed
        *args: any paramaters the function might require

    Returns: tuple of the time it takes to execute and the function result

    """
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def average(numbers):
    """
    Builds average of list numbers.
    Args:
        numbers: numbers to build average of.

    Returns:
        float of average of numbers
    """
    return sum(numbers) / float(len(numbers))


def timed_calls(n, fn, *args):
    """
        Function to return the timedcalls. If n is in, it repeats the function n times, if n is float, then it repeats
        the calls until n seconds have passed.
    Args:
        n: number of iterations
        fn: function object
        *args: function parameters

    Returns:
        Minimum, average and maximum execution time.
    """
    times = None
    if isinstance(n, int):
        times = [timed_call(fn, *args)[0] for _ in range(n)]
    if isinstance(n, float):
        passed_time = 0.0
        times = []
        while passed_time < n:
            passed_time += timed_call(fn, *args)[0]
            print(passed_time)
            times.append(timed_call(fn, *args)[0])

    return min(times), average(times), max(times)
