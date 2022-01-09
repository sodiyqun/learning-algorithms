# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 14:20:04 2022

@author: sodiyqun
"""

def yv(a,b):
    if a==0:
        return b
    elif a>b:
        a,b = b,a
    return yv(b-a, a)


def bv(a,b):
    if a==0:
        return b
    return bv(b%a, a)