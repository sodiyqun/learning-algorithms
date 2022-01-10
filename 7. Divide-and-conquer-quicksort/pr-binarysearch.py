# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:06:03 2022

@author: sodiyqun
"""

def bs(array, item, start=0, end=None):
    if end is None:
        end = len(array-1)
    if start>end:
        return None 
    
    mid = (start+end)//2
    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return bs(array, item, start, mid-1)
    elif array[mid] < item:
        return bs(array, item, mid + 1, end)
    return None