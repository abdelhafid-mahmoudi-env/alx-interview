# 0x09. Island Perimeter

## Description

This project involves calculating the perimeter of an island represented by `1`s in a grid (2D list) where `0`s represent water. The task is to write a function `island_perimeter` that returns the perimeter of the island described in the grid.

## Learning Objectives

By completing this project, you will:
- Gain experience with 2D arrays (matrices) and how to navigate through them.
- Apply conditional logic to solve geometric problems within a grid.
- Practice writing efficient algorithms to solve real-world problems.
- Reinforce Python programming skills, including nested loops and conditional statements.

## Project Requirements

- **Python Version:** Python 3.4.3
- **Operating System:** Ubuntu 20.04 LTS
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- Your code should use the PEP 8 style (version 1.7).
- You are not allowed to import any external modules.
- All modules and functions must be documented.
- All your files must be executable.

## Task

### 0. Island Perimeter

**File:** `0-island_perimeter.py`

Write a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`.

- **grid** is a list of lists of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island does not have “lakes” (water inside that isn’t connected to the water surrounding the island).

#### Example

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
