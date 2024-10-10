#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    stack = keys[:]

    while stack:
        key = stack.pop()
        if key < n and not unlocked[key]:
            unlocked[key] = True
            for new_key in boxes[key]:
                if new_key not in stack and not unlocked[new_key]:
                    stack.append(new_key)

    return all(unlocked)

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))

boxes = [[1, 2], [3], [1], []]
print(canUnlockAll(boxes))

boxes = [[1], [], [0]]
print(canUnlockAll(boxes))
