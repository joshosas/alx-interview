#!/usr/bin/python3
'''A module for working with Lockboxes.
'''

def canUnlockAll(boxes):
    '''
    Returns True if it is possible to open all boxes
    in the boxes in the given list of boxes.
    Each box contains a list of positive integers
    representing the key(s) to other boxes.
    '''
    keys = set([0])
    unlock_boxes = [0]

    while unlock_boxes:
        box_to_unlock = unlock_boxes.pop()

        for key in boxes[box_to_unlock]:
            if key not in keys:
                keys.add(key)
                
                if key < len(boxes):
                    unlock_boxes.append(key)

    return len(keys) == len(boxes)
