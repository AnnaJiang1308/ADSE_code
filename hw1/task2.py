"""
Goal of Task 2:
    Implement a function that returns the median of a list.
"""


def calc_median(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        median (type: int or float)
    """

    Len = len(list_in)
    list = sorted(list_in)
    if Len % 2 == 0:
        # even
        median = (list[int(Len / 2)] + list[int(Len / 2 - 1)]) / 2
    else:
        # odd
        median = list[int((Len - 1) / 2)]

    ########################
    #   End of your code   #
    ########################

    return median


if __name__ == "__main__":
    # Example with even number of items
    assert calc_median([0, 9, 2, 3, 1, 4, 7]) == 3

    # Example with odd number of items
    assert calc_median([0, 9, 2, 3, 1, 4, 7, 5]) == 3.5
