<<<<<<< HEAD
# Quick Sort Implementation to organize tasks by priority or time

import random

def quick_sort(activities, key):

    # Base case = if 1 or no elements, they're all sorted
    if len(activities) <= 1:
        return activities

    # List will be divided into three parts: Left, Middle, Right

    pivot = activities[len(activities) // 2][key]
    left = [x for x in activities if x[key] < pivot]    # want a smaller pivot: not smaller value but smaller index!
    middle = [x for x in activities if x[key] == pivot]
    right = [x for x in activities if x[key] > pivot]

    # Left and right lists are sorted recursively & combined together
    return quick_sort(left, key) + middle + quick_sort(right, key)
=======
# Quick Sort Implementation to organize tasks by priority or time

import random

def quick_sort(activities, key):

    # Base case = if 1 or no elements, they're all sorted
    if len(activities) <= 1:
        return activities

    # List will be divided into three parts: Left, Middle, Right

    pivot = activities[len(activities) // 2][key]
    left = [x for x in activities if x[key] < pivot]    # want a smaller pivot: not smaller value but smaller index!
    middle = [x for x in activities if x[key] == pivot]
    right = [x for x in activities if x[key] > pivot]

    # Left and right lists are sorted recursively & combined together
    return quick_sort(left, key) + middle + quick_sort(right, key)
>>>>>>> testbranch2
