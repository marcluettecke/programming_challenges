"""
Short script to solve the zebra puzzle.
"""
# imports
import itertools


def imright(h1, h2):
    """
    Function to return boolean if h1 is right to h1.
    Args:
        h1: [int] for house 1
        h2: [int] for house 2

    Returns: True if next right of other house

    """
    return h1 - h2 == 1


def nextto(h1, h2):
    """
    Function to return boolean if two houses are next to one another.
    Args:
        h1: [int] for house 1
        h2: [int] for house 2

    Returns: True if next to one another

    """
    return abs(h1 - h2) == 1


def zebra_puzzle():
    """
    Function to solve the Zebra puzzle (https://en.wikipedia.org/wiki/Zebra_Puzzle)
    Returns:
        Return a tuple (WATER, ZEBRA) indicating their house numbers.
    """

    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    # generator to save computational effort
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )
