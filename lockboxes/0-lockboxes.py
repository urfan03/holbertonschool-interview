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
  
  # While there are boxes in the queue, process them.
  while queue:
    current_box = queue.pop(0)
    
    # Check the keys available in the current box.
    for key in boxes[current_box]:
      # If the key corresponds to an unvisited box, mark it as visited and add it to the queue.
      if not visited[key]:
        visited[key] = True
        queue.append(key)
  
  # Check if all boxes have been visited (opened).
  return all(visited)