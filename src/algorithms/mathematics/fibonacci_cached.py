from functools import lru_cache

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
 """
@lru_cache
def fibonacci_cached(num):
    if num <= 1: 
        return num
    return fibonacci_cached(num - 1) + fibonacci_cached(num - 2)