""" Calculate the nth fibonacci number of the succession.

Args: 
    n_fib (int): Index of the fibbonacci succession number.

Returns:
    int: Fibonacci nth number.
"""
def fibonacci_recursive(n_fib):
    if n_fib > 1: 
        return fibonacci_recursive(n_fib - 1) + fibonacci_recursive(n_fib - 2)
    elif n_fib == 1: 
        return 1
    else: 
        return 0