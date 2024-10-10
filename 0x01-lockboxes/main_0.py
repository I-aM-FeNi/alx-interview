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

