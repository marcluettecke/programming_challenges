"""
Clever solution using splits with empty spaces to the puzzle:

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works,
give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his
runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a
paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such
rune exists.
"""


def solve_runes(runes):
    """
    Solves the puzzle to find a value digit for the expression.
    Args:
        runes: string expression to be solved.

    Returns:
        [int] that validates the expression as true
    """
    for c in sorted(set('0123456789') - set(runes)):
        s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
        if not any(e[0] == '0' and e != '0' for e in s.split()) and eval(s):
            return int(c)
    return -1
