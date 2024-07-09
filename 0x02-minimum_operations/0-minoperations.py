#!/usr/bin/python3
"""
Module for minimum operations to achieve exactly n 'H' characters.
"""


def min_operations(n):
    """
    min_operations
    Calculate the minimum number of operations.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
            divisor -= 1
        divisor += 1

    return operations
