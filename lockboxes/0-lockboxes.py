#!/usr/bin/python3


'''This script determines if all boxes can be opened.'''


def canUnlockAll(boxes):
  """
  Determines if all the boxes can be opened, considering cycle handling and efficiency.

  Args:
      boxes (list of list of int): List of boxes, each containing keys.

  Returns:
      bool: True if all boxes can be opened, False otherwise.
  """

  # Handle empty boxes case
  if not boxes:
    return False

  # Initialize visited set and a queue for exploration
  visited = set()
  queue = [0]

  # Explore the boxes efficiently using BFS
  while queue:
    current_box = queue.pop(0)
    visited.add(current_box)

    # Check if all boxes have been visited (opened)
    if len(visited) == len(boxes):
      return True

    # Explore keys with cycle handling
    for key in boxes[current_box]:
      # Skip keys outside the box range and avoid re-exploring visited boxes
      if 0 <= key < len(boxes) and key not in visited:
        queue.append(key)

  # Return False if any box is not visited
  return False

# Main function for testing with various box configurations
if __name__ == "__main__":
  # Test cases
  boxes1 = [[1], [2], [3], []]
  boxes2 = [[1], [2], [1, 2], []]
  boxes3 = [[], [], [], []]
  boxes4 = []
  for i in range(1000):
    boxes4.append([j for j in range(1000)])  # Case with all keys in each box

  print("Test 1:", canUnlockAll(boxes1))
  print("Test 2:", canUnlockAll(boxes2))
  print("Test 3:", canUnlockAll(boxes3))
  print("Test 4:", canUnlockAll(boxes4))
