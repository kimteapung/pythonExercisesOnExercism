"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(actual_min):
    """Calculate the bake time remaining.

    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - actual_min


def preparation_time_in_minutes(number_of_layers):
    """
    Return preperation time.

    :param number_of_layers: int - representing the number of layers.
    :return: int - calculates the total time it will take for layers.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    :param elapsed_bake_time: int - representing elapsed time.
    :param number_of_layers: int - representing the number of layers.
    :return: int - calculates the total elapsed minutes spent.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
