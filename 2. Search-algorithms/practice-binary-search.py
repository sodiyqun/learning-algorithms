# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 16:04:21 2022

@author: sodiyqun
"""

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99,102]

def binarySearch(name, item):
    low = 0
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = name[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
