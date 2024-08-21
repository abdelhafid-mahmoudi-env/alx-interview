# 0x08. Making Change

## Description

This project involves solving a classic problem from the domain of algorithms, particularly focusing on dynamic programming and greedy algorithms: the **coin change problem**. The goal is to find the minimum number of coins needed to make up a given total amount, using a provided list of coin denominations. The problem tests your ability to apply algorithmic strategies to achieve efficient and correct solutions.

## Learning Objectives

By completing this project, you should be able to:

- Understand and implement **greedy algorithms**.
- Recognize when a greedy algorithm might not yield the optimal solution.
- Apply **dynamic programming** to solve optimization problems.
- Analyze the **time and space complexity** of different algorithmic solutions.
- Break down complex problems into manageable sub-problems and solve them iteratively or recursively.

## Requirements

- **Editor**: vi, vim, emacs
- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- Your code should follow **PEP 8** style (version 1.7.x).
- All files must be executable.

## Project Structure

- **0-making_change.py**: This file contains the implementation of the function `makeChange(coins, total)`.
- **0-main.py**: This is a test file provided to check the functionality of the `makeChange` function.

## Function Prototype

```python
def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be achieved.

    Returns:
    int: The fewest number of coins needed to meet the total, or -1 if the total cannot be met.
    """
