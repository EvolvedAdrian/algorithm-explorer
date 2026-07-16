def fibonacci_recursive(n_fib):
    """ Calculate the nth fibonacci number of the succession.

    Time complexity:
        Best: O(1)
        Average: O(2^n)
        Worst: O(2^n)

    Space complexity: O(n)

    Args:
        n_fib (int): Index of the fibbonacci succession number.

    Returns:
        int: Fibonacci nth number.
    
    Raises:
        ValueError: If number is negative.
    """
    if n_fib < 0:
        raise ValueError("Number must be greater or equal than 0.")
    
    if n_fib in (0,1):
        return n_fib

    return fibonacci_recursive(n_fib - 1) + fibonacci_recursive(n_fib - 2)
