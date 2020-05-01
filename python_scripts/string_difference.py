"""
Function to solve the following quiz, interesting for repeated sorting methods.

Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account
the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not
consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for
string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the
maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if
this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear
with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing
order of their length and when they have the same length sorted in ascending lexicographic order (letters and digits
- more precisely sorted by codepoint); the different groups will be separated by '/'.
"""


def mix(s1, s2):
    """
    Function to compare two strings and return comparison in pre-defined output.
    Args:
        s1: string one
        s2: string two

    Returns:
        string in predefined output, with very specific ordering.
    """

    result_strings = []
    # build dictionaries with letter counts
    dict1, dict2 = {letter: s1.count(letter) for letter in s1}, {letter: s2.count(letter) for letter in s2}
    # build list of all lowercase letters of boh strings
    lowercase_letter = [letter for letter in set(s1).union(set(s2)) if letter.islower()]
    # iterate through lowercase_letters and append appropriate string
    for i, l in enumerate(lowercase_letter):
        # ignore lettercounts < 1
        if (l in dict1 and dict1[l] > 1) and (l in dict2 and dict2[l] > 1):
            # find greater count to build string
            if dict1[l] > dict2[l]:
                result_strings.append("{}:{}".format(1, l * dict1[l]))
            elif dict1[l] == dict2[l]:
                result_strings.append("=:{}".format(l * dict1[l]))
            else:
                result_strings.append("{}:{}".format(2, l * dict2[l]))
        elif (l in dict1 and dict1[l] > 1) and not (l in dict2 and dict2[l] > 1):
            result_strings.append("{}:{}".format(1, l * dict1[l]))
        elif (l in dict2 and dict2[l] > 1) and not (l in dict1 and dict1[l] > 1):
            result_strings.append("{}:{}".format(2, l * dict2[l]))
    # ordering, first (therefore conducted last and so on) by length, then by group, 1,2, or =,
    # and then alphabetically of the letter counted
    result_strings = sorted(result_strings, key=lambda entry: entry[2])
    result_strings = sorted(result_strings, key=lambda entry: 3 if entry[0] == "=" else int(entry[0]))
    return "/".join(sorted(result_strings, key=len, reverse=True))
