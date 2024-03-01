#!/usr/bin/python3


'''This script determines if all boxes can be opened.'''


def canUnlockAll(boxes):

    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes, each containing keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a stack with the first box
    stack = [0]

    while stack:
        # Pop a box from the stack
        current_box = stack.pop()
        # Mark the box as visited
        visited.add(current_box)

        # Check all keys in the current box
        for key in boxes[current_box]:
            # If the key opens a box that hasn't been visited yet
            if key < len(boxes) and key not in visited:
                stack.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))
