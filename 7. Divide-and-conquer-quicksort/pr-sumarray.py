# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:49:58 2022

@author: sodiyqun
"""

def sm(array):
    if array == []:
        return 0
    return array[0] + sm(array[1:])

ar = [5,8,6,10]
a = []
print(sm(ar))