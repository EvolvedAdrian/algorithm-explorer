""" Calculate the factorial of a number.

Args: 
    num (int): Number to calculate factorial.

Returns: 
    int: Factorial of the number.
"""
def factorial_recursive(num):
    if num > 0: 
        return num * factorial_recursive(num - 1)
    return 1