# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:34:59 2022

@author: sodiyqun
"""

from linkedlists import Node, LinkedList

llist = LinkedList()

llist.head = Node("brush teeth")
breakfast = Node("breakfast")
homework = Node("do homework")
watch = Node("watch videos")
study = Node("go to learning center")

llist.head.next = breakfast
breakfast.next = homework
homework.next = watch
watch.next = study

llist.push_b("wake up")
llist.push_e("sleep")
llist.push_m(study.data, "coding")

llist.push_m(llist.head.next.next.next.next.next.next, "play game")

llist.printlist()

print()

llist.deleteNode("play game")
llist.printlist()