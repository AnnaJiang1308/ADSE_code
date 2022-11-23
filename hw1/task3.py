"""
Goal of Task 3:
    Implement a function that returns the lowest missing number of the list, starting from 0.
"""


def lowest_missing_number(list_in):
    """
    input:
        list_in (type: list): list of integers

    output:
        lowest_number (type: int or None)
    """

    # Task:
    # ToDo: Calculate the lowest missing number of the list, starting from 0. Return "None" if there is no lowest
    #       missing number. The usage of python packages is not allowed for this task.
    # Hint: e.g. L = [3, 6, 1, 0, 9, 7, 2] the function should return 4
    ########################
    #  Start of your code  #
    ########################
    i = 0
    flag = 0
    lowest_number = 0
    while i <= max(list_in) and flag == 0:
        if (i in list_in) is False:
            flag = 1
            lowest_number = i

        i += 1

    if flag == 0:
        lowest_number = None

    ########################
    #   End of your code   #
    ########################

    return lowest_number


if __name__ == "__main__":
    assert lowest_missing_number([3, 6, 1, 0, 9, 7]) == 2
    assert lowest_missing_number([0, 1, 2, 3, 4, 5]) is None
