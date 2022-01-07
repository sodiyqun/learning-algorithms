# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 23:34:43 2022

@author: sodiyqun
"""

def fact(x):
    # print(x,end=' ')
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
        
print(fact(5))