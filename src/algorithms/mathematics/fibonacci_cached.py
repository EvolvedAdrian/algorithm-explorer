from functools import lru_cache

@lru_cache
def fibonacci_cached(num):
    """ Calculates the nth fibonacci number.
    Already calculated fibonacci values are cached using memoization.

    Time complexity:
        Best: O(1)
        Average: O(n)
        Worst: O(n)

    Space complexity: O(n)

    Args:
        num (int): Fibonacci number index.

    Returns:
        int: Fibonacci number.

    Raises:
        ValueError: If number is negative.
    """
    if num < 0:
        raise ValueError("Number must be greater or equal than 0.")
    
    if num in (0, 1):
        return num
    
    return fibonacci_cached(num - 1) + fibonacci_cached(num - 2)
