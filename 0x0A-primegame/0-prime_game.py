#!/usr/bin/python3
"""Module for determining the winner of the prime game."""


def isWinner(x, nums):
    """Determines the winner."""
    mariaWins = 0
    benWins = 0

    for num in nums:
        roundsSet = list(range(1, num + 1))
        primesSet = in_range(1, num)

        if not primesSet:
            benWins += 1
            continue

        isMariaTurn = True

        while(True):
            if not primesSet:
                if isMariaTurn:
                    benWins += 1
                else:
                    mariaWins += 1
                break

            smallestPrime = primesSet.pop(0)
            roundsSet.remove(smallestPrime)

            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurn = not isMariaTurn

    if mariaWins > benWins:
        return "Winner: Maria"

    if mariaWins < benWins:
        return "Winner: Ben"

    return None


def isprime(n):
    """Checks if a number n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def in_range(start, end):
    """Generates a list of prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end+1) if isprime(n)]
