#!/usr/bin/python3


'''This script determines if all boxes can be opened.'''


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened, considering cycle handling.

    Args:
        boxes (list of list of int): List of boxes, each containing keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    if not boxes:
        return False

    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        if len(visited) == len(boxes):
            return True

        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and key not in visited:
                queue.append(key)

    return False

if __name__ == "__main__":
    boxes1 = [[1], [2], [3], []]
    boxes2 = [[1], [2], [1, 2], []]
    boxes3 = [[], [], [], []]
    boxes4 = []
    for i in range(1000):
        boxes4.append([j for j in range(1000)])

    print("Test 1:", canUnlockAll(boxes1))
    print("Test 2:", canUnlockAll(boxes2))
    print("Test 3:", canUnlockAll(boxes3))
    print("Test 4:", canUnlockAll(boxes4))
