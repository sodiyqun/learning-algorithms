# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:36:14 2022

@author: sodiyqun
"""

## Find the biggest

# 1. start
# 2. create var. x, y, z
# 3. give value to x, y, z
# 4. if x > y:
#       if x > z then return x as biggest
#       else return z as biggist
# 5. else (i.e. x < y):
#       if y > z then return y as biggest
#       else return z as biggest


def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c