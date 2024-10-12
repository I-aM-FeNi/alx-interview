#!/usr/bin/python3
"""
main_0.py

This script tests the canUnlockAll function from the 0-lockboxes module.
"""

# Import the canUnlockAll function from the 0-lockboxes module
canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1: Sequentially unlocked boxes
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 2: Boxes with multiple keys and some redundant keys
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 3: Not all boxes can be unlocked
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False

# Additional test cases
boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False

boxes = [[0]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [
    [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [],
    [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6],
    [9, 5, 8, 8], [6, 2, 8, 6]
]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [
    [7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3],
    [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7],
    [4, 2, 9, 6, 6, 5, 5]
]
print(canUnlockAll(boxes))  # Expected output: False
