"""
Solution to following problem using bitwise operations ^= to flip bits and conversion to int to increase performance:

Given a binary number, we are about to do some operations on the number. Two types of operations can be here:

['I', i, j] : Which means invert the bit from i to j (inclusive).

['Q', i] : Answer whether the i'th bit is 0 or 1.

The MSB (most significant bit) is the first bit (i.e. i = 1). The binary number can contain leading zeroes.
"""
# imports
import numpy as np


def binary_simulation(s, b):
    """
    Conducts operations on a bitwise string, such as inverting parts and returning  bit from a given index.
    Args:
        s: string bits, such as "1000101"
        b: list of commands, such as [['I', 2, 3], ['Q',5]]

    Returns:
        List with answers to the Q commands.
    """
    # initializes empty result list and an np array which maps the string bits into integers
    a, r = np.fromiter(map(int, s), dtype=np.int), []
    for x in b:
        if x[0] == "Q":
            r.append(str(a[x[1] - 1]))
        else:
            # retrieve the (weird) indexes from command
            i, j = x[1:]
            # flip bits in place for the subpart of np.array that is defined by indexes
            a[i - 1:j] ^= 1
    return r
