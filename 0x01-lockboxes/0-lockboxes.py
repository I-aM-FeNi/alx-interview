#!/usr/bin/python3
def canUnlockAll(boxes):

    opened = set()
    stack = [0]
    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key not in opened:
                    stack.append(key)

    return len(opened) == len(boxes)


# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
