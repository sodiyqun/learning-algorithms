# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 03:42:02 2022

@author: sodiyqun
"""

class Stack():
    """Stack object"""
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack)==0
    
    def push(self, data):
        self.stack.append(data)
        return print("Appended")

    def pop(self):
        if self.isEmpty():
            return print("Stack is empty")
        else:
            return self.stack.pop()
            
    def peek(self):
        if self.isEmpty():
            return print("Stack is empty")
        else:
            return self.stack[-1]