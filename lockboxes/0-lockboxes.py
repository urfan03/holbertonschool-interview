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

    num_boxes = len(boxes)
    num_keys = sum(len(box) for box in boxes)

    # If the total number of keys exceeds or equals the number of boxes,
    # then all boxes can be opened.
    if num_keys >= num_boxes:
        return True

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
            if key < num_boxes and key not in visited:
                stack.append(key)

    # If all boxes have been visited, return True
    return len(visited) == num_boxes


# Example usage:
if __name__ == "__main__":
    boxes = []

    keys = []
    for n in range(1, 1000):
        keys = []
        for m in range(1, 1000):
            keys.append(m)
        boxes.append(keys)

    print(canUnlockAll(boxes))
