"""
Goal of Task 4:
"""


def fibonacci(n):
    """
    input:
        n (type: int)

    output:
        fibonacci_number (type: int)
    """

    # Task:
    # ToDo: Calculate the n-th number of the Fibonacci Sequence.
    #       The usage of python packages is not allowed for this task.
    # Hint: F_n = F_n-1 + F_n-2
    ########################
    #  Start of your code  #
    ########################
    Temp1 = 1
    Temp2 = 1

    fibonacci_number = 0

    if n == 1 or n == 2:
        fibonacci_number = 1
    else:
        for i in range(n - 2):
            fibonacci_number = Temp1 + Temp2
            Temp1 = Temp2
            Temp2 = fibonacci_number
            i += 1

    ########################
    #   End of your code   #
    ########################

    return fibonacci_number


if __name__ == "__main__":
    assert fibonacci(9) == 34
