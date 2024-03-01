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

    visited = set()

    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                stack.append(key)

    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], []]
    keys = [[1], [2], [3], []]

    for n in range(1, 1000):
        keys = []

        for m in range(1, 1000):

            keys.append(m)
            boxes.append(keys)

    print(canUnlockAll(boxes))
