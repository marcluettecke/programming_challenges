"""
Function to shift every letter by 13 positions in the alphabet. Clever use of maketrans and translate.
"""

trans = str.maketrans('ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
                      'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')


def rot13(message):
    """
    Translation by rot13 encoding.
    Args:
        message: string such as 'Test'

    Returns:
        translated string, such as 'Grfg'
    """
    return message.translate(trans)
