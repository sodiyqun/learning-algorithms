# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:29:09 2022

@author: sodiyqun
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push_b(self, new_data):
        """add in the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def push_m(self, prev_node, new_data):      # you can use path or also key
        """add in the middle"""
        if prev_node is None:
                return None
        new_node = Node(new_data)
        
        if type(prev_node) is str:              # if you used key
            temp = self.head
            while temp:
                if temp.data == prev_node:
                    break
                temp = temp.next
            if temp == None:
                return
            new_node.next = temp.next
            temp.next = new_node
        else:                                   # if you used path
            new_node.next = prev_node.next
            prev_node.next = new_node
    
    def push_e(self, new_data):
        """add in the end"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def deleteNode(self, key):
        """delete linkeds"""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None