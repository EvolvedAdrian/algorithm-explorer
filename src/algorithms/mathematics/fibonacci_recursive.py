def fibonacci_recursive(n_fib):
    """ Calculate the nth fibonacci number of the succession.

    Time complexity:
        Best: O(1)
        Average: O(2n)
        Worst: O(2n)

    Space complexity: O(n)

    Args:
        n_fib (int): Index of the fibbonacci succession number.

    Returns:
        int: Fibonacci nth number.
    """
    if n_fib > 1:
        return fibonacci_recursive(n_fib - 1) + fibonacci_recursive(n_fib - 2)
    elif n_fib == 1: 
        return 1
    else: 
        return 0