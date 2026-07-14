def factorial_recursive(num):
    """ Calculate the factorial of a number.

    Time complexity:
        Best: O(1)
        Average: O(n)
        Worst: O(n)

    Space complexity: O(n)

    Args:
        num (int): Number to calculate factorial.

    Returns:
        int: Factorial of the number.
    """
    if num > 0:
        return num * factorial_recursive(num - 1)
    return 1