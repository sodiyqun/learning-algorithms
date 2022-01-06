# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 13:28:32 2022

@author: sodiyqun
"""

def findmax(array):
    maks = array[0]
    max_index = 0
    for n in range(1, len(array)):
        if array[n] > maks:
            maks = array[n]
            max_index = n
    return max_index

def selectionSort(array):
    newArray = []
    for n in range(len(array)):
        max_index = findmax(array)
        newArray.append(array.pop(max_index))
    return newArray



r = [2,5,8,7,6,1,9,4,3]