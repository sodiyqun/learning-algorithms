# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 10:14:15 2022

@author: sodiyqun
"""

myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
name = myList1
def linearSearch(name, item):
    for n in range(len(name)):
        if name[n] == item:
            return n
        
    return None