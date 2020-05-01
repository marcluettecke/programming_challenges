"""
Clever solution for the mexican wave.
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a
string and you must return that string in an array where an uppercase letter is a person standing up.
"""


def wave(s):
    """
    Solution utilizing capitalize and isalpha() string methods to implement the Mexican wave.
    Args:
        s: string to be replaced

    Returns:
        list of strings with always one letter capitalized sequentially.
    """
    return [s[:index].lower() + s[index:].capitalize() for index, value in enumerate(list(s)) if s[index].isalpha()]

