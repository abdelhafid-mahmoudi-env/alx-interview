# Prime Game

This project is part of the ALX curriculum, focusing on algorithms and game theory using Python. The challenge involves determining the winner of a competitive game between Maria and Ben, based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

## Table of Contents
- [Introduction](#introduction)
- [Concepts Needed](#concepts-needed)
  - [Prime Numbers](#prime-numbers)
  - [Sieve of Eratosthenes](#sieve-of-eratosthenes)
  - [Game Theory](#game-theory)
  - [Dynamic Programming/Memoization](#dynamic-programmingmemoization)
  - [Python Programming](#python-programming)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Prime Game](#0-prime-game)
- [Usage](#usage)
- [License](#license)

## Introduction

Maria and Ben are playing a game where they take turns choosing a prime number from a set of consecutive integers. After a prime is chosen, that number and all its multiples are removed from the set. The player who cannot make a move loses. The game is played over multiple rounds, and the goal is to determine the overall winner assuming both players play optimally.

## Concepts Needed

### Prime Numbers
- **Definition:** A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
- **Algorithms:** Efficient algorithms are needed to identify prime numbers within a range.

### Sieve of Eratosthenes
- **Definition:** An ancient algorithm used to find all primes up to a given limit.
- **Usage:** Highly efficient for generating a list of primes, which is essential for solving this problem.

### Game Theory
- **Definition:** The study of mathematical models of strategic interaction among rational decision-makers.
- **Application:** Understanding optimal strategies for the game and win conditions.

### Dynamic Programming/Memoization
- **Definition:** A method for solving problems by breaking them down into simpler subproblems and storing the results to avoid redundant calculations.
- **Application:** Optimizing the solution for multiple rounds of the game.

### Python Programming
- **Core Concepts:** Loops, conditional statements, lists, and arrays are essential for implementing the game logic and algorithms.

## Requirements

- **Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS with Python 3 (version 3.4.3)
- **Code Style:** PEP 8 (version 1.7.x)
- **Files:** All files must be executable and end with a new line.
- **Mandatory Files:** A `README.md` file at the root of the project directory.

## Tasks

### 0. Prime Game

- **Objective:** Determine the winner of the game for `x` rounds.
- **Prototype:** `def isWinner(x, nums)`
  - `x`: Number of rounds
  - `nums`: Array of integers representing the end number of each round.
- **Return:** Name of the player who won the most rounds (`"Maria"` or `"Ben"`). If the winner cannot be determined, return `None`.

**Example:**
```python
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print("Winner:", result)  # Output: Ben
