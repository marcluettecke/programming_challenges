"""
Solution to the following problem, utilizing combinations library and default behavior:

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum
sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are
positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest
possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null,
None, Nothing, depending on the language. With C++, C, Rust, Swift, Go, Kotlin return -1.

Examples:

ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163
"""

from itertools import combinations


def choose_best_sum(t, k, ls):
    """
    Function the return the largest value of k elements in ls array if sum is less than t.
    Args:
        t: [int] limiting sum factor
        k: [int] number of array elements
        ls: [List[int]] list of elements to choose from

    Returns:
        int of best value
    """
    return max((sum(v) for v in combinations(ls, k) if sum(v) <= t), default=None)
