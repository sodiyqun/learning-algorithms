# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:24:13 2022

@author: sodiyqun
"""

## Algorithm for getting sum two numb.

# 1. start
# 2. create num1, num2 and sumtwo variables
# 3. accept numbers
# 4. sum up nembers, result we'll load to var: sumtwo
# 5. return sumtwo to user
# 6. stop


num1 = int(input("write 1st number: "))
num2 = int(input("write 2nd number: "))
sumtwo = num1 + num2
print(sumtwo)

# or 

def addNums(a,b):
    summa = a + b
    return summa