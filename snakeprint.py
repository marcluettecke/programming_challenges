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
    # while there are still elements in the array
    while array:
        # get the entire first row
        a.extend(list(array.pop(0)))
        # match the nested list with its counterparts, meaning [[1,2], becomes [[1,3],
        #                                                       [3,4]]          [2,4]]
        array = list(zip(*array))
        # reverse the list to [[2,4],
        #                      [1,3]]
        array.reverse()
    return a
