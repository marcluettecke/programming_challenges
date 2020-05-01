"""
Function to solve the following puzzle with a generator.
------------------
User Instructions

Hopper, Kay, Liskov, Perlis, and Ritchie live on
different floors of a five-floor apartment building.
Hopper does not live on the top floor.
Kay does not live on the bottom floor.
Liskov does not live on either the top or the bottom floor.
Perlis lives on a higher floor than does Kay.
Ritchie does not live on a floor adjacent to Liskov's.
Liskov does not live on a floor adjacent to Kay's.

Where does everyone live?

Write a function floor_puzzle() that returns a list of
five floor numbers denoting the floor of Hopper, Kay,
Liskov, Perlis, and Ritchie.
"""

# imports
import itertools


def is_adjacent(floor1, floor2):
    """
    Function to determine if two floors are adjacent.
    Args:
        floor1: [int] level of floor 1
        floor2: [int] level of floor 2

    Returns:
        [bool] if two floors are adjacent
    """
    return abs(floor1 - floor2) == 1


def floor_puzzle():
    """
    Function to include a bunch of restrictions on 5 inhabitants and find the solution by brute force or possible
    permutations.
    Returns:
        [List] of the five floor numbers for the five people in the order: [Hopper, Kay, Liskov, Perlis, Ritchie]
    """
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))

    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
                for [Hopper, Kay, Liskov, Perlis, Ritchie] in orderings
                # Hopper does not live on the top floor.
                if Hopper is not bottom
                # Kay does not live on the bottom floor.
                if Kay is not bottom
                # Liskov does not live on either the top or the bottom floor.
                if Liskov not in [bottom, top]
                # Perlis lives on a higher floor than does Kay.
                if Perlis > Kay
                # Ritchie does not live on a floor adjacent to Liskov's.
                if is_adjacent(Ritchie, Liskov) == False
                # Liskov does not live on a floor adjacent to Kay's.
                if is_adjacent(Liskov, Kay) == False)
