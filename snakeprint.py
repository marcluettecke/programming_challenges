"""
Toy method to return an array of nested lists printed out in a snake-like format. Useful list methods included.
"""


def snail(array):
    """
    Function to return a nested array in snake format, circling from the outside to the inside as 1-dimensional array.
    Args:
        array: nxn array of nested lists (rows, columns)

    Returns:
        n**2 long array including the snake formatted original array.
    """
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a
