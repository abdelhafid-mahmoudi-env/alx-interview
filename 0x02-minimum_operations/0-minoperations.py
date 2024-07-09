#!/usr/bin/python3
"""
Function that calculates the minimum number
of operations to achieve exactly n 'H' characters.
"""


def minOperations(n):
    operations_count = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations_count += divisor
            n /= divisor
        divisor += 1
    return operations_count
