"""
Function to evaluate cryptometric problems, in the form of 'ODD + ODD == EVEN' , i.e. which number combination would
evaluate this string as true if it replaced the letters.
"""

import re, itertools


def solve(formula):
    """
    Solver function which validates a string that describes a python statement and replacec capital letters with digits.
    Args:
        formula: The string of a statement to be solved. Example: 'AB is not in [DD, FF, G]'

    Returns:
        [str] with filled in digits
    """
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    """
    Generator to fill in all possible combinations of digits for the capital letters in string.
    Args:
        formula: String, for which letters need to be replaced.

    Yields:
        one possible combination of digits filled in for the letters.
    """
    letters = "".join(set("".join(re.findall("[A-Z]+", formula))))
    # print(letters)
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """
    Function to check if the statement is valid, i.e. if it evaluates to true and if the digits do not start with a 0.
    Args:
        f: string of a python statement

    Returns:
        [bool] if statement evaluares to true or false
    """
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
