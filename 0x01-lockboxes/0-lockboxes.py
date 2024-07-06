#!/usr/bin/python3
"""
Solution to the lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False

    for key in range(1, len(boxes) - 1):
        is_box_checked = False
        for box_index in range(len(boxes)):
            is_box_checked = key in boxes[box_index] and key != box_index
            if is_box_checked:
                break
        if is_box_checked is False:
            return is_box_checked
    return True
