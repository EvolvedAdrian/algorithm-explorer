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

    Raises:
        ValueError: If number is negative.
    """
    if num < 0:
        raise ValueError("Number must be greater or equal than 0.")
    
    if num in (0, 1):
        return 1
    
    return num * factorial_recursive(num - 1)
