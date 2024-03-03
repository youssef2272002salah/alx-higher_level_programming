#!/usr/bin/python3
""" a module that defines find_peak function"""


def find_peak(arr):
    """ find peak """
    for i in range(len(arr) - 1):
        if i == 0 and arr[i] > arr[i + 1]:
            return arr[i]
        elif i == len(arr) - 2 and arr[i] < arr[i + 1]:
            return arr[i + 1]
        elif i > 0 and arr[i - 1] < arr[i] > arr[i + 1]:
            return arr[i]
    return None
