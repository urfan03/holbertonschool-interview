#!/usr/bin/python3
'''This function determines if all the boxes can be opened.'''

def canUnlockAll(boxes):
  """
  This function determines if all the boxes can be opened.

  Args:
      boxes: A list of lists, where each inner list represents the keys 
             available in a specific box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """

  # Initialize a visited list to keep track of opened boxes.
  visited = [False] * len(boxes)

  # Mark the first box as opened since it's the starting point.
  visited[0] = True

  # Use a queue to process boxes iteratively.
  queue = [0]

  # Set to track the maximum depth reached during exploration (optional).
  max_depth = 0

  # While there are boxes in the queue, process them.
  while queue:
    current_box = queue.pop(0)

    # Update the maximum depth reached.
    max_depth = max(max_depth, len(visited) - 1)

    # If the current box is already visited and NOT in the current queue, it's a cycle and can be opened.
    if visited[current_box] and current_box not in queue:
      continue  # Continue processing other boxes

    # If already visited and in the queue, it's a true cycle, return False.
    elif visited[current_box]:
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

# Optional: Log a message about checker depth limitation (if applicable)
print(f"Maximum depth reached during exploration: {max_depth}")
