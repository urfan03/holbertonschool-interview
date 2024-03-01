#!/usr/bin/python3

def canUnlockAll(boxes):
  """
  This function determines if all the boxes can be opened.

  Args:
      boxes: A list of lists, where each inner list represents the keys 
             available in a specific box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """

  # Mark the first box as visited (opened) since it's the starting point.
  visited = [False] * len(boxes)
  visited[0] = True

  # Use a queue to process boxes iteratively.
  queue = [0]

  # Keep track of the maximum depth reached during exploration.
  max_depth = 0

  # While there are boxes in the queue, process them.
  while queue:
    current_box = queue.pop(0)

    # Update the maximum depth reached.
    current_depth = len(visited) - 1
    max_depth = max(max_depth, current_depth)

    # If a cycle is detected (current box is already marked as visited), return False.
    if visited[current_box]:
      return False

    # Mark the current box as visited.
    visited[current_box] = True

    # Check the keys available in the current box.
    for key in boxes[current_box]:
      # If the key corresponds to an unvisited box, add it to the queue.
      if not visited[key]:
        queue.append(key)

  # Check if all boxes have been visited (opened).
  return all(visited)

# Example usage
boxes = [
    [1, 2, 3],
    [3],
    [0],
]

if canUnlockAll(boxes):
  print("All boxes can be opened.")
else:
  print("Not all boxes can be opened.")

# Optional: Log a message about checker depth limitation (if applicable)
print(f"Maximum depth reached during exploration: {max_depth}")
